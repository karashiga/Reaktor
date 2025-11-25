#!/usr/bin/env python3
"""
fb_auto_react_cookies.py
Termux-ready multi-account Facebook auto-react tool using cookie -> access token.

Features:
 - Convert your Facebook cookie to a user access token (no password used)
 - Store multiple accounts in accounts.json
 - Add / Remove / List / Check accounts
 - Auto-react to a public post (LIKE, LOVE, HAHA, WOW, SAD, ANGRY)
 - Per-account limits and delays
 - Detect & optionally remove dead tokens

Usage:
 - python3 fb_auto_react_cookies.py
"""

import os
import re
import json
import time
import random
import requests
from typing import List, Dict, Tuple

ACCOUNTS_FILE = "accounts.json"
GRAPH_VER = "v17.0"
GRAPH_BASE = f"https://graph.facebook.com/{GRAPH_VER}"
USER_AGENT = "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Mobile Safari/537.36"

REACTION_TYPES = {
    "1": "LIKE",
    "2": "LOVE",
    "3": "HAHA",
    "4": "WOW",
    "5": "SAD",
    "6": "ANGRY",
}
REACTION_NAMES = {v: k for k, v in REACTION_TYPES.items()}

# ----------------- Persistence helpers -----------------
def load_accounts() -> List[Dict]:
    if not os.path.exists(ACCOUNTS_FILE):
        return []
    try:
        with open(ACCOUNTS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def save_accounts(accounts: List[Dict]):
    with open(ACCOUNTS_FILE, "w") as f:
        json.dump(accounts, f, indent=2)

def add_account(name: str, token: str):
    accounts = load_accounts()
    accounts.append({"name": name, "token": token})
    save_accounts(accounts)
    print(f"[+] Added account '{name}'")

def remove_account(index: int) -> bool:
    accounts = load_accounts()
    if 0 <= index < len(accounts):
        removed = accounts.pop(index)
        save_accounts(accounts)
        print(f"[-] Removed account '{removed.get('name')}'")
        return True
    return False

# ----------------- Cookie -> Token conversion -----------------
def cookie_to_token(cookie: str, timeout: float = 10.0) -> Tuple[bool, str]:
    """
    Try to convert a valid Facebook mobile cookie to a user access token.
    This uses public mobile endpoints and parses an accessToken value from the response.
    Returns (success, token_or_error)
    """
    cookie = cookie.strip()
    if not cookie or "=" not in cookie:
        return False, "Invalid cookie string"

    headers = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://m.facebook.com/",
        "Cookie": cookie
    }

    endpoints = [
        # common endpoint used in some token-getter patterns
        "https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed",
        # a fallback endpoint that may contain tokens in some responses
        "https://m.facebook.com/connect/prompt_overlays?__a=1",
        # Graph mobile composer endpoint (may or may not return token)
        "https://m.facebook.com/api/graphql/"
    ]

    for url in endpoints:
        try:
            resp = requests.get(url, headers=headers, timeout=timeout)
            text = resp.text or ""
            # Heuristic: look for "accessToken":"E..." or "accessToken":"EAAB..."
            m = re.search(r'"accessToken"\s*:\s*"([^"]+)"', text)
            if m:
                token = m.group(1)
                return True, token
            # Some responses contain "access_token":"EAA..." (without camelCase)
            m2 = re.search(r'"access_token"\s*:\s*"([^"]+)"', text)
            if m2:
                token = m2.group(1)
                return True, token
            # Sometimes token is embedded as accessToken=... in JS
            m3 = re.search(r"accessToken=([A-Za-z0-9\-_\.]+)", text)
            if m3:
                return True, m3.group(1)
            # Some pages include "EAAB" style tokens plain in JSON - look for long E.. token
            m4 = re.search(r'(E[A-Za-z0-9]{50,})', text)
            if m4:
                return True, m4.group(1)
        except requests.RequestException as e:
            # try next endpoint
            continue

    return False, "Failed to extract token. Cookie might be invalid or Facebook changed endpoint responses."

# ----------------- Graph interactions -----------------
def check_token(token: str, timeout: float = 8.0) -> Tuple[bool, Dict]:
    try:
        url = f"{GRAPH_BASE}/me"
        resp = requests.get(url, params={"access_token": token, "fields": "id,name"}, timeout=timeout)
        data = resp.json()
        if resp.status_code == 200 and "id" in data:
            return True, data
        else:
            return False, data
    except requests.RequestException as e:
        return False, {"error": str(e)}

def react_post(token: str, post_id: str, reaction_type: str, timeout: float = 8.0) -> Tuple[bool, Dict]:
    try:
        url = f"{GRAPH_BASE}/{post_id}/reactions"
        resp = requests.post(url, data={"type": reaction_type, "access_token": token}, timeout=timeout)
        try:
            data = resp.json()
        except ValueError:
            data = {"raw": resp.text, "status_code": resp.status_code}
        if resp.status_code in (200, 201) and (data == {} or data.get("success") or "id" in data):
            return True, data
        else:
            return False, data
    except requests.RequestException as e:
        return False, {"error": str(e)}

# ----------------- Utilities -----------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def extract_post_id(link_or_id: str) -> str:
    link = link_or_id.strip()
    if link.isdigit():
        return link
    # common patterns
    patterns = [
        r"facebook\.com/.+?/posts/([0-9]+)",
        r"facebook\.com/permalink\.php\?story_fbid=([0-9]+)&id=[0-9]+",
        r"facebook\.com/.+?/videos/([0-9]+)",
        r"story_fbid=([0-9]+)",
        r"ft_ent_identifier=([0-9]+)",
    ]
    for p in patterns:
        m = re.search(p, link)
        if m:
            return m.group(1)
    # fallback: return original input (may be short code but attempt)
    return link_or_id

# ----------------- CLI actions -----------------
def show_accounts():
    accounts = load_accounts()
    if not accounts:
        print("[!] No accounts stored yet.")
        return
    print("Stored accounts:")
    for i, acc in enumerate(accounts):
        token_preview = acc.get("token", "")[:10] + "..." if acc.get("token") else "(no token)"
        print(f" {i}. {acc.get('name','(no name)')} - {token_preview}")

def interactive_add_cookie():
    print("Paste your Facebook cookie (from your browser). Example: c_user=...; xs=...; datr=...;")
    cookie = input("Cookie: ").strip()
    if not cookie:
        print("[!] Cookie empty. Aborting.")
        return
    print("[*] Attempting to get access token from cookie. Please wait...")
    ok, result = cookie_to_token(cookie)
    if not ok:
        print(f"[!] Token extraction failed: {result}")
        return
    token = result
    # Quick check
    ok2, info = check_token(token)
    if ok2:
        print(f"[+] Token OK for user: {info.get('name')} (id {info.get('id')})")
    else:
        print(f"[!] Token created but /me check failed: {info}")
        # still allow add if user wants
        cont = input("Save token anyway? [y/N]: ").strip().lower()
        if cont != "y":
            return
    name = input("Label for this account (eg. 'me', 'phone', 'acc1'): ").strip() or info.get("name", "me")
    add_account(name, token)

def interactive_add_manual_token():
    name = input("Label for this account: ").strip() or "unnamed"
    token = input("Paste access token: ").strip()
    if not token:
        print("[!] Token empty.")
        return
    ok, info = check_token(token)
    if ok:
        print(f"[+] Token valid for {info.get('name')}")
        add_account(name, token)
    else:
        print(f"[!] Token check failed: {info}")
        cont = input("Save token anyway? [y/N]: ").strip().lower()
        if cont == "y":
            add_account(name, token)

def interactive_remove():
    accounts = load_accounts()
    if not accounts:
        print("[!] No accounts to remove.")
        return
    show_accounts()
    try:
        idx = int(input("Index to remove: ").strip())
    except ValueError:
        print("[!] Invalid input.")
        return
    if not remove_account(idx):
        print("[!] Index out of range.")

def check_all_tokens(remove_dead: bool = False):
    accounts = load_accounts()
    if not accounts:
        print("[!] No accounts stored.")
        return
    alive = []
    dead = []
    print("[*] Checking tokens...")
    for acc in accounts:
        ok, info = check_token(acc["token"])
        if ok:
            print(f"[OK] {acc.get('name')} -> {info.get('name')} (id {info.get('id')})")
            alive.append(acc)
        else:
            print(f"[BAD] {acc.get('name')} -> {info}")
            dead.append(acc)
    print(f"\nSummary: {len(alive)} alive, {len(dead)} dead.")
    if remove_dead and dead:
        save_accounts(alive)
        print(f"[!] Removed {len(dead)} dead accounts from {ACCOUNTS_FILE}.")

def run_auto_react():
    accounts = load_accounts()
    if not accounts:
        print("[!] No accounts stored. Add one via cookie or manual token first.")
        return

    post_input = input("Enter target post link or post id: ").strip()
    if not post_input:
        print("[!] Empty post. Aborting.")
        return
    post_id = extract_post_id(post_input)
    reaction_choice = input("Choose reactions (comma numbers like 1,2 or 'all')\n"
                            "1=LIKE 2=LOVE 3=HAHA 4=WOW 5=SAD 6=ANGRY\n"
                            "Choice [default all]: ").strip().lower() or "all"
    selected_reactions = []
    if reaction_choice == "all":
        selected_reactions = list(REACTION_TYPES.values())
    else:
        parts = [p.strip() for p in reaction_choice.split(",") if p.strip()]
        for p in parts:
            if p in REACTION_TYPES:
                selected_reactions.append(REACTION_TYPES[p])
    if not selected_reactions:
        print("[!] No valid reactions chosen. Aborting.")
        return

    try:
        per_account = int(input("Reactions per account (default 1): ").strip() or "1")
        if per_account < 1: per_account = 1
    except ValueError:
        per_account = 1

    try:
        delay = float(input("Delay between each reaction in seconds (default 1.0): ").strip() or "1.0")
        if delay < 0: delay = 1.0
    except ValueError:
        delay = 1.0

    # Validate accounts before run
    live_accounts = []
    dead_accounts = []
    print("[*] Validating accounts...")
    for acc in accounts:
        ok, info = check_token(acc["token"])
        if ok:
            live_accounts.append((acc, info))
        else:
            dead_accounts.append((acc, info))
    if dead_accounts:
        print(f"[!] {len(dead_accounts)} dead/invalid tokens found and will be skipped.")
        rem = input("Remove dead tokens from storage? [y/N]: ").strip().lower()
        if rem == "y":
            accounts = [a for a, _ in live_accounts]
            save_accounts(accounts)
            print("[+] Dead tokens removed.")

    total_attempted = 0
    total_success = 0
    try:
        for acc, info in live_accounts:
            name = acc.get("name", "unnamed")
            token = acc["token"]
            print(f"\n--> Using account: {name} (id: {info.get('id')})")
            success_for_account = 0
            for i in range(per_account):
                # choose reaction type (random from selected list) to avoid identical pattern if multiple reactions allowed
                reaction_type = random.choice(selected_reactions) if len(selected_reactions) > 1 else selected_reactions[0]
                ok, resp = react_post(token, post_id, reaction_type)
                total_attempted += 1
                if ok:
                    success_for_account += 1
                    total_success += 1
                    print(f"   [+] {reaction_type} succeeded ({i+1}/{per_account})")
                else:
                    print(f"   [!] {reaction_type} failed ({i+1}/{per_account}) -> {resp}")
                    # if token invalid, break from this account
                    if isinstance(resp, dict) and resp.get("error") and resp["error"].get("code") in (190,):
                        print("   [!] Token invalid/expired. Skipping remaining actions for this account.")
                        break
                time.sleep(delay)
            print(f"   -> Account summary: {success_for_account}/{per_account} success")
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")

    print(f"\nFinished. Attempts: {total_attempted}, Successes: {total_success}")

# ----------------- Main Menu -----------------
def main_menu():
    while True:
        clear_screen()
        print("=== FB Auto React (cookie -> token) ===")
        print("1) Add account via cookie (recommended)")
        print("2) Add account manually (paste token)")
        print("3) Show accounts")
        print("4) Remove account")
        print("5) Check all tokens (detect dead)")
        print("6) Run auto-react")
        print("7) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            interactive_add_cookie()
            input("\nPress Enter to continue...")
        elif choice == "2":
            interactive_add_manual_token()
            input("\nPress Enter to continue...")
        elif choice == "3":
            show_accounts()
            input("\nPress Enter to continue...")
        elif choice == "4":
            interactive_remove()
            input("\nPress Enter to continue...")
        elif choice == "5":
            check_all_tokens(remove_dead=False)
            input("\nPress Enter to continue...")
        elif choice == "6":
            run_auto_react()
            input("\nPress Enter to continue...")
        elif choice == "7":
            print("Bye.")
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()
