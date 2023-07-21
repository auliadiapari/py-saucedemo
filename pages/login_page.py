from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import base_page_locators, base_page_users

class login_page:
    def __init__ (self, driver):
        self.driver = webdriver.Firefox()

    def go_to_page(self):
        self.driver.get('https://saucedemo.com')
    
    def input_username(self, username):
        self.driver.find_element(usname_field).send_keys(username)
    
    def input_password(self, password):
        self.driver.find_element(psswod_field).send_keys(password)

    def click_login_button(self, login):
        self.driver.find_element(login_button).click()
    
    def verify_home_page(self):
        page_title = self.driver.find_element(By.XPATH, '//*[@class="title"]')
        page_title == "Products"
        print("Login Successfully")





        

        
        