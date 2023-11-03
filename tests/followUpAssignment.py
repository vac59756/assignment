from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load flipkart.com desktop home page
driver.get("https://www.flipkart.com/")

# Create a list with parameters
product_info = []

#Using try catch to differentate platform based on elements
# Search for the product "Samsung Galaxy S10"
try:
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.submit()

    time.sleep(2)
    # Click on "Mobiles" in categories
    category = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Mobiles']"))
    )
    category.click()

    # Apply Filters
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

    for name, price, link in zip(product_names, product_prices, product_links):
        product_info.append({
        "Product Name": name.text,
        "Product Price": ((price.text).split('\n'))[0],
        "Link to Product Details Page": link.get_attribute("href")
    })
    
    # Print the list on the console
    for item in product_info:
        print(item)
except:
    search_box_device = driver.find_element(By.XPATH, "//div[text()='Search for Products, Brands and More']")
    search_box_device.click()
    time.sleep(1)
    search_box2_device = driver.find_element(By.ID, "input-searchsearchpage-input")
    search_box2_device.send_keys("Samsung Galaxy S10")
    search_box2_device.submit()

    time.sleep(3)
    # Apply Filters
    filter = driver.find_element(By.XPATH, "//div[text()='Filter']")
    filter.click()
    time.sleep(1)

    # Select SAMSUNG brand
    brand = driver.find_element(By.XPATH, "//div[text()='Brand']")
    brand.click()
    time.sleep(1)

    brand_samsung = driver.find_element(By.XPATH, "//div[text()='SAMSUNG']")
    brand_samsung.click()

    # Select Flipkart assuared
    filter_fassuared = driver.find_element(By.XPATH,f"//div[@class='css-1dbjc4n']//div[text()='Plus (FAssured)']")
    filter_fassuared.click()
    time.sleep(1)
    
    filter_fassuared_checkbox = driver.find_elements(By.XPATH,f"//div[@class='css-1dbjc4n']//div[text()='Plus (FAssured)']")[1]
    filter_fassuared_checkbox.click()

    #Apply the filters
    apply = driver.find_element(By.XPATH, "//div[text()='Apply ']")
    apply.click()

    #Steps here to extract details from page
    

# Close the WebDriver
driver.quit()