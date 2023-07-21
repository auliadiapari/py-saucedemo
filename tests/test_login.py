from pages.login_page import LoginPage


class testLoginPage:

    def testValidLogin(self):
        LoginPage.go_to_page()
        LoginPage.input_password()
        LoginPage.input_password()
        LoginPage.input_password()
        LoginPage.click_login_button()
        LoginPage.verify_home_page()

testLoginPage.testValidLogin()
        

