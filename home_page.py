import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@type='search']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//div[@class='product-action']/button")
    CART_ICON = (By.CSS_SELECTOR, "img[alt='Cart']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def search_product(self, product_name):
        logging.info(f"Searching for product: {product_name}")
        search_input = self.safe_find_element(*self.SEARCH_INPUT)
        search_input.clear()  # Clear any pre-filled text
        search_input.send_keys(product_name)
        time.sleep(3)  # Allow time for products to appear
    def add_products_to_cart(self):
        logging.info("Adding products to cart")
        buttons = self.safe_find_elements(*self.ADD_TO_CART_BUTTON)
        print(f"Found {len(buttons)} 'Add to Cart' buttons")
        for button in buttons:
            # Wait until each button is clickable
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-action']/button")))
            button.click()

    def go_to_cart(self):
        logging.info("Navigating to cart")
        self.safe_find_element(*self.CART_ICON).click()
        self.safe_find_element(*self.CHECKOUT_BUTTON).click()
