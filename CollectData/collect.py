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

# Create the directory if it doesn't exist
#os.makedirs(os.path.dirname(Data_Set_path), exist_ok=True)

# Options 
option = Options()
# option.add_argument("--headless=new")

service = Service(executable_path=PATH)
driver = webdriver.Chrome(options=option, service=service)

def SaveToFile(file, elements):
    with open(file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for element in elements:
            writer.writerow([element.text])  # Save the text content of the elements

try:
    driver.get(URL)
    
    time.sleep(10)  # Allow time for the page to load
    filter_class = driver.find_elements(By.CSS_SELECTOR, ".row1, .row2, .row3, .row4, .row5, .row6") 
    
    SaveToFile(Data_Set_path, filter_class)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
