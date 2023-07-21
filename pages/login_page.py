from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page import BasePageUsers, BasePageLocators


class LoginPage(BasePageUsers, BasePageLocators):

    def go_to_page(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://saucedemo.com')
    
    def input_username(self):
        usname_input = self.driver.find_element(BasePageUsers.usname_field)
        usname_input.send_keys(BasePageUsers.username)
    
    def input_password(self):
        psswod_input = self.driver.find_element(BasePageUsers.psswod_field)
        psswod_input.send_keys(BasePageUsers.password)

    def click_login_button(self):
        button_login = self.driver.find_element(BasePageLocators.login_button)
        button_login.click()
    
    def verify_home_page(self):
        page_title = self.driver.find_element(By.XPATH, '//*[@class="title"]')
        page_title == "Products"
        print("Login Successfully")



        

        
        