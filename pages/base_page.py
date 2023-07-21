from selenium.webdriver.common.by import By


class BasePageUsers:
    username = "standard_user"
    password = "secre_sauce"

class BasePageLocators:
    usname_field = (By.ID, 'user-name')
    psswod_field = (By.ID, 'password')
    login_button = (By.ID, 'login-button')