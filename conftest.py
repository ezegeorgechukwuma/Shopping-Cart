import pytest
import logging

# import pytest_html
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
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # Log to console
            logging.FileHandler("test_log.log", mode="w"),  # Log to file
        ],
    )
    logger = logging.getLogger()  # Root logger
    logger.setLevel(logging.INFO)
    logging.info("Logging setup is complete")
