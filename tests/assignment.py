from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load flipkart.com desktop home page
driver.get("https://www.flipkart.com/")

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
brand = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='SAMSUNG']"))
)
brand.click()

time.sleep(2)

flipkart_assured_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3U-Vxu"))
)
flipkart_assured_filter.click()

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

# Close the WebDriver
driver.quit()
