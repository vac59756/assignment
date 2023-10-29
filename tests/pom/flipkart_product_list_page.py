from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartProductListPage:

    def __init__(self, driver):
        self.driver = driver
        self.category_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Mobiles']"))
        )

    def go_to_mobiles_category(self):
        self.category_link.click()