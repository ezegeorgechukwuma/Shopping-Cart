import logging
import time
import conftest

from selenium.webdriver.common.by import By

from home_page import HomePage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shopping_cart(driver):
    logging.info("Starting shopping cart test")

    home_page = HomePage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Open the URL
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")

    # Search and add items to cart
    home_page.search_product("ber")
    home_page.add_products_to_cart()
    home_page.go_to_cart()

    # Validate total amount
    total_price = cart_page.calculate_total()
    displayed_total = cart_page.get_total_amount_displayed()
    assert total_price == displayed_total, f"Expected {total_price}, but got {displayed_total}"

    # Proceed to checkout, apply promo code, and place the order
    checkout_page.apply_promo_code("rahulshettyacademy")
    assert "Code applied" in driver.find_element(By.CLASS_NAME,"promoInfo").text
    # assert "Code applied" in driver.find_element_by_class_name("promoInfo").text
    time.sleep(4)
    checkout_page.place_order("Nigeria")
    time.sleep(10)
    logging.info("Completed shopping cart test")
