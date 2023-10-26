import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

#import environment variables
userName = os.environ['BROWSERSTACK_USERNAME']
accessKey = os.environ['BROWSERSTACK_ACCESS_KEY']
localIdentifier = os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
buildName = os.environ['BROWSERSTACK_BUILD_NAME']
projectName = os.environ['BROWSERSTACK_PROJECT_NAME']

#set capabilities
bstack_options = {
    "os" : "Windows",
    "osVersion" : "10",
    "buildName" : "Build Name: " + buildName,
    "projectName" : "Project Name: " + projectName,
    "localIdentifier": localIdentifier,
    "seleniumVersion" : "4.0.0",
    "userName": userName,
    "accessKey": accessKey
}

options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)
driver.get("https://www.flipkart.com/") # HTTP Server should be running on 8099 port of GitHub runner
driver.maximize_window()

# Search for the product "Samsung Galaxy S10"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Samsung Galaxy S10")
search_box.submit()

# Click on "Mobiles" in categories
category = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Mobiles']"))
)
category.click()

# Apply filters
# Select SAMSUNG brand
brand = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='SAMSUNG']"))
)
brand.click()

time.sleep(2)

# Select Flipkart assuared
flipkart_assured_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3U-Vxu"))
)
flipkart_assured_filter.click()

#Sort price high to low
high_to_low_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Price -- High to Low']"))
)
high_to_low_option.click()

time.sleep(2)

# Read the set of results on page 1
product_names = driver.find_elements(By.CLASS_NAME, '_4rR01T')
product_prices = driver.find_elements(By.CLASS_NAME, '_25b18c')
product_links = driver.find_elements(By.CLASS_NAME, '_1fQZEK')

# Create a list with parameters
product_info = []

for name, price, link in zip(product_names, product_prices, product_links):
    product_info.append({
        "Product Name": name.text,
        "Product Price": ((price.text).split('\n'))[0],
        "Link to Product Details Page": link.get_attribute("href")
    })
	
# Print the list on the console
for item in product_info:
    print(item)

#Execute the test using BrowserStack Automate platform
if product_info:
    # Set the status of test as 'passed'
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Product details were gathered"}}')
else:
    # Set the status of test as 'failed'
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Product details failed to gather"}}')


# Close the WebDriver
driver.quit()
