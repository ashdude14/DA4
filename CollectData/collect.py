import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time

PATH = "chromedriver.exe"
URL = "https://www.naukri.com/data-analyst-jobs"
Data_Set_path = "../DataSet/data.csv"

# Ensure the directory exists
os.makedirs(os.path.dirname(Data_Set_path), exist_ok=True)

# Options 
option = Options()
# option.add_argument("--headless=new")

service = Service(executable_path=PATH)
driver = webdriver.Chrome(options=option, service=service)

def SaveToFile(file, elements):
    with open(file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for element in elements:
            # Extract the text content of the element and split into lines
            text_content = element.text.strip().split('\n')
            
            # Join the text content into a single row with fields separated by commas
            formatted_row = [", ".join(text_content)]  # Use "|" or another delimiter
            
            # Write the row to the CSV file
            writer.writerow(formatted_row)

try:
    driver.get(URL)
    time.sleep(10)  # Allow time for the page to load
    
    filter_class = driver.find_elements(By.CSS_SELECTOR, ".row1, .row2, .row3, .row4, .row5, .row6") 
    
    SaveToFile(Data_Set_path, filter_class)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
