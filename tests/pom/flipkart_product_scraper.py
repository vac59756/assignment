from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flipkart_home_page import FlipkartHomePage
from flipkart_product_list_page import FlipkartProductListPage
from flipkart_product_details_page import FlipkartProductDetailsPage
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load flipkart.com desktop home page
driver.get("https://www.flipkart.com/")

# Create instances of Page Objects
home_page = FlipkartHomePage(driver)

# Use Page Objects to interact with the page
home_page.search_product("Samsung Galaxy S10")

product_list_page = FlipkartProductListPage(driver)
product_list_page.go_to_mobiles_category()

# ... (Apply filters, sort, etc.)
brand_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@title='SAMSUNG']"))
)
brand_filter.click()

time.sleep(2)

flipkart_assured_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_3U-Vxu"))
)
flipkart_assured_filter.click()

time.sleep(2)

# Sort by Price (High to Low)
high_to_low_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Price -- High to Low']"))
)
high_to_low_option.click()

time.sleep(2)

# Create instance of Product Details Page
product_details_page = FlipkartProductDetailsPage(driver)

# Get product information
product_info = product_details_page.get_product_info()

# Print the list on the console
for item in product_info:
    print(item)

# Close the WebDriver
driver.quit()