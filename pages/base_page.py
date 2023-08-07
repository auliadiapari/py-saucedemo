from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=5):
        Wait = WebDriverWait
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))


class BasePageUsers:
    STANDARD_USERNAME = "standard_user"
    LOCKED_USER = "locked_out_user"
    PROBLEM_USER = "secret_sauce"
    PERFORMANCE_GLITCH_USER = "secret_sauce"

    ALL_USER_PASSWORD = "secret_sauce"


class BasePageLocators:

    # URL
    BASE_URL = 'https://saucedemo.com'

    # Login locators & elements
    USERNAME_FIELD = ('id', 'user-name')
    PASSWORD_FIELD = ('id', 'password')
    LOGIN_BUTTON = ('id', 'login-button')
    LOGIN_LOGO = ('xpath', '//div [@class="login_logo"]')

    # Inventory Page
    INV_PAGE_TITLE = ('xpath', '//div [@class="header_secondary_container"]')
    INV_PAGE_SHOPCART = ('id', 'shopping_cart_container')
    INV_PAGE_SORT_CONTAINER = ('xpath', '//select [@class="product_sort_container"]')
    # Inventory Page - Menu
    INV_PAGE_MENU = ('id', 'react-burger-menu-btn')
    INV_PAGE_MENU_ITEMS = ('id', 'inventory_sidebar_link')
    INV_PAGE_MENU_ABOUT = ('id', 'about_sidebar_link')
    INV_PAGE_MENU_LOGOUT = ('id', 'logout_sidebar_link')

    # Cart Page
    CART_PAGE_TITLE = ('xpath', '//div [@class="header_secondary_container"]')
    CART_PAGE_CHECKOUT = ('id', 'checkout')
    CART_PAGE_CONTINUE_SHOPPING = ('id', 'continue-shopping')

    # Checkout Page
    CHECKOUT_PAGE_TITLE = ('xpath', '//div [@class="header_secondary_container"]')

        # Checkout Info
    CHECKOUT_FNAME_FIELD = ('id', 'first-name')
    CHECKOUT_LNAME_FIELD = ('id', 'last-name')
    CHECKOUT_PCODE_FIELD = ('id', 'postal-name')

    CHECKOUT_PAGE_CONTINUE = ('id', 'continue')
    CHECKOUT_PAGE_CANCEL = ('id', 'cancel')

        # Checkout Overview
    CHECKOUT_PAGE_FINISH = ('id', 'finish')

        # Checkout Complete
    CHECKOUT_PAGE_COMPLETE = ('id', 'checkout_complete_container')
    CHECKOUT_PAGE_BACK_HOME = ('id', 'back-to-products')



