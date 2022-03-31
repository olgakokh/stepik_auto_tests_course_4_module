from .base_page import BasePage
from .locators import LoginPageLocators
import time, random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Error in URL ADRESS"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Error in LOGIN FORM"
      

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Error in REGISTER FORM"

    def register_new_user(self, email, password):
        input1 = self.browser.find_element(*LoginPageLocators.LOG_REG_ADDRESS)
        input1.click()
        email = str(time.time()) + "@fakemail.org"
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.LOG_REG_PASSWORD)
        input2.click()
        password = str(time.time() + random.randrange(500))
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.LOG_REG_PASSWORD_DOUBLE)
        input3.click()
        input3.send_keys(password)
        button_log_reg = self.browser.find_element(*LoginPageLocators.LOG_REG_BUTTON)
        button_log_reg.click()





     