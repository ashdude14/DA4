from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

PATH="cd.exe"

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Example of adding an option
chrome_options.add_argument("--disable-infobars")  # Disable the 'controlled by automation' banner
chrome_options.add_argument("--disable-notifications")  # Suppress notifications
chrome_options.add_argument("--start-maximized")  # Start maximized
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--headless")  # Optional: Run in headless mode


# Initialize the WebDriver
service = Service(PATH)  # Use Service class for ChromeDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")
print(driver.title)

# Close the browser
driver.quit()