#!/usr/bin/env python3
import os, json, requests, time

ACCOUNTS_FILE = "accounts.json"

# Load accounts
def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return []
    with open(ACCOUNTS_FILE, "r") as f:
        return json.load(f)

# Save accounts
def save_accounts(data):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Get Graph API Token using DB-LN cookie
def get_token_from_cookie(dbln):
    try:
        cookies = {"dbln": dbln}
        
        # Official Facebook mobile token endpoint
        url = "https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed"
        r = requests.get(url, cookies=cookies)

        token = None
        if "EAA" in r.text:
            token = r.text.split("EAA")[1].split('"')[0]
            token = "EAA" + token

        return token
    except:
        return None

# Add account
def add_account():
    os.system("clear")
    print("=== ADD FACEBOOK ACCOUNT USING DB-LN COOKIE ===\n")
    dbln = input("Paste DB-LN cookie: ").strip()

    print("\nGetting Graph API Token...")
    token = get_token_from_cookie(dbln)

    if not token:
        print("❌ Failed to get token. Cookie invalid.")
        time.sleep(2)
        return

    accounts = load_accounts()
    accounts.append({"dbln": dbln, "token": token})
    save_accounts(accounts)

    print("\n✅ Account added successfully!")
    print("Saved token: " + token[:20] + "...")
    time.sleep(2)

# React to a post
def react_to_post():
    os.system("clear")
    print("=== AUTO REACT TO PUBLIC POST ===\n")
    post_id = input("Enter Facebook Post Link or ID: ").strip()
    reaction = input("Reaction (LIKE, LOVE, WOW, HAHA, SAD, ANGRY): ").upper()

    accounts = load_accounts()
    if len(accounts) == 0:
        print("\n❌ No accounts stored!")
        time.sleep(2)
        return

    print(f"\nUsing {len(accounts)} accounts...\n")

    for idx, acc in enumerate(accounts, start=1):
        token = acc["token"]
        url = f"https://graph.facebook.com/{post_id}/reactions"
        payload = {
            "type": reaction,
            "access_token": token
        }

        r = requests.post(url, data=payload)

        if r.status_code == 200:
            print(f"[{idx}] ✅ Reacted successfully.")
        else:
            print(f"[{idx}] ❌ Failed: {r.text}")

        time.sleep(1)

    input("\nDone! Press Enter...")

# Dashboard / Menu
def menu():
    while True:
        os.system("clear")
        accounts = load_accounts()
        total = len(accounts)

        print("======================================")
        print(" FACEBOOK AUTO REACTION TOOL (Termux) ")
        print("======================================")
        print(f"Total Accounts Saved: {total}")
        print("--------------------------------------")
        print("[1] Add Account (DB-LN Cookie)")
        print("[2] Auto React to Post")
        print("[3] Exit")
        print("--------------------------------------")
        choice = input("Select: ")

        if choice == "1":
            add_account()
        elif choice == "2":
            react_to_post()
        elif choice == "3":
            exit()
        else:
            print("Invalid Option!")
            time.sleep(1)

if __name__ == "__main__":
    menu()
