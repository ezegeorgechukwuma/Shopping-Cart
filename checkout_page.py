# pages/checkout_page.py
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from base_page import BasePage

class CheckoutPage(BasePage):
    PROMO_CODE_INPUT = (By.CSS_SELECTOR, ".promoCode")
    PROMO_BUTTON = (By.CSS_SELECTOR, ".promoBtn")
    PROMO_INFO = (By.CSS_SELECTOR, ".promoInfo")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Place Order']")
    COUNTRY_DROPDOWN = (By.XPATH, "//div[@class='wrapperTwo']//div//select")
    CHECK_AGREE = (By.XPATH, "//input[@class='chkAgree']")
    PROCEED_BUTTON = (By.XPATH, "//button[normalize-space()='Proceed']")

    def apply_promo_code(self, promo_code):
        logging.info(f"Applying promo code: {promo_code}")
        self.safe_find_element(*self.PROMO_CODE_INPUT).send_keys(promo_code)
        self.safe_find_element(*self.PROMO_BUTTON).click()
        self.wait_for_element(*self.PROMO_INFO)

    def place_order(self, country):
        logging.info("Placing order and selecting country")
        self.safe_find_element(*self.PLACE_ORDER_BUTTON).click()
        dropdown = Select(self.safe_find_element(*self.COUNTRY_DROPDOWN))
        dropdown.select_by_visible_text(country)
        self.safe_find_element(*self.CHECK_AGREE).click()
        self.safe_find_element(*self.PROCEED_BUTTON).click()
