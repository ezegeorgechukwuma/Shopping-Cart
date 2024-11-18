# pages/cart_page.py
import logging
from selenium.webdriver.common.by import By
from base_page import BasePage

class CartPage(BasePage):
    PRICE = (By.CSS_SELECTOR, "tr td:nth-child(5) p")
    TOTAL_AMOUNT = (By.CSS_SELECTOR, ".totAmt")

    def calculate_total(self):
        logging.info("Calculating total from item prices")
        prices = self.safe_find_elements(*self.PRICE)
        total = sum(int(price.text) for price in prices)
        return total

    def get_total_amount_displayed(self):
        logging.info("Fetching displayed total amount")
        return int(self.safe_find_element(*self.TOTAL_AMOUNT).text)
