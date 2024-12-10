from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

PATH="chromedriver.exe"
URL="https://www.naukri.com/data-analyst-jobs"
filter_class="styles_filterCount__Xn_PG"
filter_par="styles_ellipsis__cvWP1 styles_filterLabel__jRP04"
cont_list="cust-job-tuple layout-wrapper lay-2 sjw__tuple"
#options 

option=Options()
#option.add_argument("--headless=new")


service=Service(executable_path=PATH)
driver=webdriver.Chrome(options=option,service=service)

try:
    driver.get(URL)
    
except Exception as e:
    print(e)
finally:
    time.sleep(10)
    filter_class=driver.find_elements(By.CSS_SELECTOR,".row1, .row2,.row3, .row4, .row5, .row6") 
    #filter_class.click()
    count=0
    for element in filter_class : 
        print(element.text)
        count+=1
    print('total counts= ',count)
    driver.quit()

   