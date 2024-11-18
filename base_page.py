import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def safe_find_element(self, by, locator, retries=3):
        """Find a single element with retries to handle stale element exceptions."""
        for attempt in range(retries):
            try:
                element = self.driver.find_element(by, locator)
                return element
            except StaleElementReferenceException:
                logging.warning(f"StaleElementReferenceException encountered. Retrying... (Attempt {attempt + 1})")
                time.sleep(1)
        raise Exception(f"Element with locator {locator} could not be found after {retries} retries")

    def safe_find_elements(self, by, locator, retries=3):
        """Find multiple elements with retries to handle stale element exceptions."""
        for attempt in range(retries):
            try:
                elements = self.driver.find_elements(by, locator)
                return elements
            except StaleElementReferenceException:
                logging.warning(f"StaleElementReferenceException encountered. Retrying... (Attempt {attempt + 1})")
                time.sleep(1)
        raise Exception(f"Elements with locator {locator} could not be found after {retries} retries")
