from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

PATH="chromedriver.exe"




service=Service(executable_path=PATH)
driver=webdriver.Chrome(service=service)

try:
    driver.get("https://www.github.com/ashdude14/DA4")
except Exception as e:
    print(e)
finally:
    print(driver.title)
    driver.quit()

   