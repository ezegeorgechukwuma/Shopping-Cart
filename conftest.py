import pytest
import logging
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function", autouse=True)
def setup_logging():
    logging.basicConfig(
        filename="test_log.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    yield
