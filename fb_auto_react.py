import requests
import json
import time

# List of multiple tokens (each token = 1 Facebook account)
TOKEN_FILE = "tokens.txt"

def load_tokens():
    try:
        with open(TOKEN_FILE, "r") as f:
            return [t.strip() for t in f.readlines() if t.strip()]
    except FileNotFoundError:
        print("[!] tokens.txt not found.")
        return []

def save_token(token):
    with open(TOKEN_FILE, "a") as f:
        f.write(token + "\n")

def react_with_token(token, post_id, reaction_type):
    url = f"https://graph.facebook.com/{post_id}/reactions"
    params = {
        "type": reaction_type.upper(),
        "access_token": token
    }

    response = requests.post(url, data=params)

    try:
        data = response.json()
    except:
        return False, "Invalid JSON response from FB"

    if "success" in data and data["success"] is True:
        return True, "Reacted successfully"
    else:
        return False, str(data)

def auto_react():
    tokens = load_tokens()
    if not tokens:
        print("No tokens available in tokens.txt")
        return

    post_id = input("Enter Facebook PUBLIC post ID: ")
    reaction_type = input("Choose reaction (LIKE, LOVE, WOW, HAHA, SAD, ANGRY, CARE): ").upper()

    for i, token in enumerate(tokens):
        print(f"\n[{i+1}] Using token: {token[:20]}...")

        success, message = react_with_token(token, post_id, reaction_type)

        if success:
            print("   ✔", message)
        else:
            print("   ✘ Failed:", message)

        time.sleep(1)  # Avoid spamming API

def add_account():
    token = input("Paste your Facebook access token: ")
    save_token(token)
    print("[+] Token saved!")

def menu():
    while True:
        print("\n=== AUTO FB REACTION TOOL ===")
        print("1. Add Account Token")
        print("2. Auto React to Post")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_account()
        elif choice == "2":
            auto_react()
        else:
            break

if __name__ == "__main__":
    menu()
