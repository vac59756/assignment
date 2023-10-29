from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartHomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

    def search_product(self, query):
        self.search_box.send_keys(query)
        self.search_box.submit()