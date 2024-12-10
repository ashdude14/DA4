from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

PATH="chromedriver.exe"
URL="https://www.naukri.com/data-analyst-jobs"
search_bar_class="nI-gNb-search-bar"
#options 

option=Options()
option.headless=True


service=Service(executable_path=PATH)
driver=webdriver.Chrome(options=option,service=service)

try:
    driver.get(URL)
    
except Exception as e:
    print(e)
finally:
    time.sleep(10)
    filter_class=driver.find_element(By.CLASS_NAME,search_bar_class)
    #filter_class.click()
    print(filter_class)
    driver.quit()

   