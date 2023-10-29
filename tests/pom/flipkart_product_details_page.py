from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartProductDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_names = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, '_4rR01T'))
        )
        self.product_prices = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, '_25b18c'))
        )
        self.product_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, '_1fQZEK'))
        )

    def get_product_info(self):
        product_info = []
        for name, price, link in zip(self.product_names, self.product_prices, self.product_links):
            product_info.append({
                "Product Name": name.text,
                "Product Price": ((price.text).split('\n'))[0],
                "Link to Product Details Page": link.get_attribute("href")
            })
        return product_info