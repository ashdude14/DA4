import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Configuration
PATH = "chromedriver.exe"
URL = "https://www.naukri.com/data-analyst-jobs"
Data_Set_path = "../DataSet/data.csv"

# Ensure the directory exists
os.makedirs(os.path.dirname(Data_Set_path), exist_ok=True)

# Initialize Selenium WebDriver
options = Options()
# options.add_argument("--headless=new")  # Uncomment for headless mode
service = Service(executable_path=PATH)
driver = webdriver.Chrome(options=options, service=service)

def save_to_file(file, elements):
    """Save extracted data to the CSV file."""
    with open(file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for element in elements:
            text_content = element.text.strip().split('\n')
            formatted_row = [" | ".join(text_content)]
            writer.writerow(formatted_row)

def extract_and_save_data():
    """Extract and save data from the current page."""
    try:
        # Find data elements
        data_elements = driver.find_elements(By.CSS_SELECTOR, ".row1, .row2, .row3, .row4, .row5, .row6")
        save_to_file(Data_Set_path, data_elements)
    except Exception as e:
        print(f"Error during data extraction: {e}")

def close_popups():
    """Close any blocking pop-ups or overlays."""
    try:
        popup_close_button = driver.find_element(By.CSS_SELECTOR, ".styles_ppContainer__eeZyG .close-button")
        popup_close_button.click()
        print("Pop-up dismissed.")
    except NoSuchElementException:
        print("No pop-up to close.")

try:
    driver.get(URL)
    time.sleep(5)  # Allow the page to load

    # Initialize CSV with headers (optional)
    with open(Data_Set_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Job Details"])  # Add headers if needed

    while True:
        # Extract and save data from the current page
        extract_and_save_data()

        try:
            # Handle any pop-ups
            close_popups()

            # Locate the "Next" button
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/.."))
            )

            # Scroll to and click the "Next" button
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            driver.execute_script("arguments[0].click();", next_button)

            # Wait for the next page to load
            time.sleep(5)

        except TimeoutException:
            print("No more pages to navigate.")
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
