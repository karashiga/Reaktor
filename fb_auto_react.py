#!/usr/bin/env python3
import os
import json
import requests
import time

ACCOUNTS_FILE = "accounts.json"
GRAPH_API = "https://graph.facebook.com"

def load_accounts():
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=2)

def get_token_from_cookie(dbln):
    cookies = {"dbln": dbln}
    try:
        url = "https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed"
        r = requests.get(url, cookies=cookies)
        text = r.text
        if "EAA" in text:
            token = "EAA" + text.split("EAA")[1].split('"')[0]
            return token
    except Exception as e:
        print("Error getting token:", e)
    return None

def add_account():
    os.system("clear")
    print("=== ADD ACCOUNT ===\n")
    dbln = input("Paste DB-LN cookie: ").strip()
    name = input("Enter a name for this account: ").strip()

    print("\nGetting Graph API token …")
    token = get_token_from_cookie(dbln)
    if not token:
        print("❌ Failed to get token. Cookie invalid.")
        time.sleep(2)
        return

    accounts = load_accounts()
    accounts.append({"dbln": dbln, "token": token, "name": name})
    save_accounts(accounts)

    print("\n✅ Account added!")
    print("Token prefix:", token[:20], "…")
    time.sleep(2)

def react_to_post():
    os.system("clear")
    print("=== AUTO REACT ===\n")
    post = input("Enter public post URL or ID: ").strip()
    reaction = input("Enter reaction (LIKE, LOVE, WOW, HAHA, SAD, ANGRY, CARE): ").upper()

    accounts = load_accounts()
    if not accounts:
        print("❌ No accounts in config.")
        time.sleep(2)
        return

    post_id = post.split("/")[-1].split("?")[0] if "/" in post else post
    print(f"\nUsing {len(accounts)} accounts …\n")

    for i, acc in enumerate(accounts, start=1):
        token = acc.get("token")
        name = acc.get("name", "<no name>")
        print(f"[{i}] Reacting with {name} …")

        url = f"{GRAPH_API}/{post_id}/reactions"
        data = {"type": reaction, "access_token": token}
        r = requests.post(url, data=data)

        try:
            resp = r.json()
        except:
            resp = {}

        if r.status_code == 200 and "error" not in resp:
            print("   ✅ Success")
        else:
            print("   ❌ Failed:", resp)

        time.sleep(1)

    input("\nDone. Press Enter to return to menu…")

def show_accounts():
    os.system("clear")
    print("=== SAVED ACCOUNTS ===\n")
    accounts = load_accounts()
    if not accounts:
        print("No accounts saved.\n")
    else:
        for i, acc in enumerate(accounts, start=1):
            name = acc.get("name", "<no name>")
            token = acc.get("token", "")
            print(f"[{i}] {name} — token prefix: {token[:20]}…")
    input("\nPress Enter to go back…")

def delete_account():
    accounts = load_accounts()
    if not accounts:
        print("❌ No accounts to delete.")
        time.sleep(2)
        return
    show_accounts()
    idx = input("Enter account number to delete: ").strip()
    try:
        idx = int(idx) - 1
        if 0 <= idx < len(accounts):
            removed = accounts.pop(idx)
            save_accounts(accounts)
            print(f"✅ Removed account: {removed.get('name')}")
        else:
            print("❌ Index out of range.")
    except ValueError:
        print("❌ Invalid input.")
    time.sleep(2)

def menu():
    while True:
        os.system("clear")
        accounts = load_accounts()
        print("===== FB AUTO REACT TOOL =====")
        print(f"Accounts saved: {len(accounts)}")
        print("[1] Add account")
        print("[2] Show accounts")
        print("[3] Auto react to post")
        print("[4] Delete account")
        print("[0] Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            add_account()
        elif choice == "2":
            show_accounts()
        elif choice == "3":
            react_to_post()
        elif choice == "4":
            delete_account()
        elif choice == "0":
            break
        else:
            print("❌ Invalid choice.")
            time.sleep(1)

if __name__ == "__main__":
    menu()
