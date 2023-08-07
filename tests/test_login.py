import time

import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePageLocators, BasePageUsers
from pages.login_page import LoginPage


@pytest.mark.usefixtures('driver_init')
class TestLogin:

    @pytest.mark.tc01
    def test_standard_user(self):
        self.driver.get(BasePageLocators.BASE_URL)

        LoginPage(self.driver).verify_login_page()
        LoginPage(self.driver).enter_username(BasePageUsers.STANDARD_USERNAME)
        LoginPage(self.driver).enter_password(BasePageUsers.ALL_USER_PASSWORD)
        LoginPage(self.driver).click_login_button()
        LoginPage(self.driver).verify_success_login()

    @pytest.mark.tc02
    def test_locked_out_user(self):
        self.driver.get(BasePageLocators.BASE_URL)

        LoginPage(self.driver).verify_login_page()
        LoginPage(self.driver).enter_username(BasePageUsers.LOCKED_USER)
        LoginPage(self.driver).enter_password(BasePageUsers.ALL_USER_PASSWORD)
        LoginPage(self.driver).click_login_button()
        LoginPage(self.driver).verify_success_login()

    @pytest.mark.tc03
    def test_problem_user(self):
        LoginPage(self.driver).verify_login_page()
        LoginPage(self.driver).enter_username(BasePageUsers.PROBLEM_USER)
        LoginPage(self.driver).enter_password(BasePageUsers.ALL_USER_PASSWORD)
        LoginPage(self.driver).click_login_button()
        LoginPage(self.driver).verify_success_login()

    @pytest.mark.tc04
    def test_performance_glitch_user(self):
        LoginPage(self.driver).verify_login_page()
        LoginPage(self.driver).enter_username(BasePageUsers.PERFORMANCE_GLITCH_USER)
        LoginPage(self.driver).enter_password(BasePageUsers.ALL_USER_PASSWORD)
        LoginPage(self.driver).click_login_button()
        LoginPage(self.driver).verify_success_login()




