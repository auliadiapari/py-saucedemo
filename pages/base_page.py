from selenium.webdriver.common.by import By


class base_page_users:
    username = "standard_user"
    password = "secre_sauce"

class base_page_locators:
    usname_field = (By.ID, 'user-name')
    psswod_field = (By.ID, 'password')
    login_button - (By.ID, 'login-button')

