#!/usr/bin/env python3
import requests
import json
import os
import time

ACCOUNTS_FILE = "accounts.json"

# ---------------------------------------
# Load accounts file
# ---------------------------------------
def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return []
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)

def save_accounts(data):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------------------------------
# Check account status
# ---------------------------------------
def check_account(cookie):
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get("https://mbasic.facebook.com/profile.php", headers=headers)

    if "Add Friend" in r.text or "Profile" in r.text:
        return "active"
    if "Your Account Has Been Disabled" in r.text:
        return "dead"
    if "login" in r.url:
        return "locked"
    return "unknown"


# ---------------------------------------
# React function
# ---------------------------------------
def send_reaction(cookie, post_id, reaction):
    session = requests.Session()
    session.headers.update({
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0"
    })

    # Step 1: Open the reaction link
    url = f"https://mbasic.facebook.com/reactions/picker/?ft_id={post_id}"
    page = session.get(url).text

    # Reaction IDs
    react_map = {
        "like": "1",
        "love": "2",
        "care": "16",
        "haha": "4",
        "wow": "3",
        "sad": "7",
        "angry": "8"
    }

    if reaction not in react_map:
        return False, "Invalid reaction"

    react_code = react_map[reaction]

    # Search the reaction link
    import re
    match = re.search(r'href="([^"]+)&reaction_type=' + react_code, page)
    if not match:
        return False, "Cannot find reaction link"

    react_link = "https://mbasic.facebook.com" + match.group(1).replace("&amp;", "&") + f"&reaction_type={react_code}"

    session.get(react_link)
    return True, "Reacted!"


# ---------------------------------------
# Add new account
# ---------------------------------------
def add_account():
    print("\nEnter DBLN Cookie:")
    cookie = input("Cookie: ")

    print("Checking account...")
    status = check_account(cookie)
    print("Status:", status)

    data = load_accounts()
    data.append({"cookie": cookie, "status": status})
    save_accounts(data)

    print("Account saved!\n")


# ---------------------------------------
# Remove dead accounts
# ---------------------------------------
def clean_dead():
    data = load_accounts()
    new = [acc for acc in data if acc["status"] == "active"]
    removed = len(data) - len(new)

    save_accounts(new)
    print(f"\nRemoved: {removed} dead/locked accounts\n")


# ---------------------------------------
# Recheck all accounts
# ---------------------------------------
def refresh_status():
    data = load_accounts()
    active = dead = locked = 0

    print("\nChecking all accounts...\n")
    for acc in data:
        s = check_account(acc["cookie"])
        acc["status"] = s
        if s == "active":
            active += 1
        elif s == "dead":
            dead += 1
        elif s == "locked":
            locked += 1

    save_accounts(data)

    print("Active:", active)
    print("Dead:", dead)
    print("Locked:", locked)
    print()


# ---------------------------------------
# Auto Reaction
# ---------------------------------------
def auto_react():
    post_id = input("\nEnter Post ID: ")
    reaction = input("Reaction (like/love/haha/wow/sad/angry/care): ")
    limit = int(input("Limit number of reactions: "))

    data = load_accounts()
    count = 0

    for acc in data:
        if acc["status"] != "active":
            continue

        if count >= limit:
            break

        ok, msg = send_reaction(acc["cookie"], post_id, reaction)
        print(f"[{acc['status']}] {msg}")

        count += 1
        time.sleep(2)

    print(f"\nTotal reactions sent: {count}\n")


# ---------------------------------------
# Main Menu
# ---------------------------------------
def main():
    while True:
        print("""
====== FACEBOOK AUTO REACT ======
1. Add FB Account (DBLN Cookie)
2. Auto React on Public Post
3. Remove Dead/Locked Accounts
4. Refresh Account Status
5. Show Statistics
0. Exit
""")
        c = input("Choose: ")

        if c == "1":
            add_account()
        elif c == "2":
            auto_react()
        elif c == "3":
            clean_dead()
        elif c == "4":
            refresh_status()
        elif c == "5":
            stats()
        elif c == "0":
            exit()


# ---------------------------------------
# Stats
# ---------------------------------------
def stats():
    data = load_accounts()
    active = sum(1 for a in data if a["status"] == "active")
    dead = sum(1 for a in data if a["status"] == "dead")
    locked = sum(1 for a in data if a["status"] == "locked")

    print("\n===== ACCOUNT STATUS =====")
    print("Active Accounts :", active)
    print("Dead Accounts   :", dead)
    print("Locked Accounts :", locked)
    print("Total Accounts  :", len(data))
    print()


if __name__ == "__main__":
    main()
