from pages.base_page import BasePage, BasePageUsers, BasePageLocators


class LoginPage(BasePage, BasePageUsers, BasePageLocators):

    def verify_login_page(self):
        loginPage = self.wait_for_element(self.LOGIN_LOGO).text
        if loginPage == "Swag Labs":
            print("Successfully go to Login Page")
        else:
            print(" Not Successfully go to Login Page")

    def enter_username(self, username):
        usrnameField = self.wait_for_element(self.USERNAME_FIELD)
        usrnameField.send_keys(username)

    def enter_password(self, password):
        psswordField = self.wait_for_element(self.PASSWORD_FIELD)
        psswordField.send_keys(password)

    def click_login_button(self,):
        loginButton = self.wait_for_element(self.LOGIN_BUTTON)
        loginButton.click()

    def verify_success_login(self):
        afterSuccessLoginPage = self.wait_for_element(self.INV_PAGE_TITLE).text
        if afterSuccessLoginPage == "Products":
            print("Successfully go to Login Page")
        else:
            print(" Not Successfully go to Login Page")
