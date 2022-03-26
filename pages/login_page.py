from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверкa на корректный url адрес
        login_url = self.browser.current_url
        assert "login" in login_url, "Error in URL ADRESS"

    def should_be_login_form(self):
        # проверкa, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Error in LOGIN FORM"
      

    def should_be_register_form(self):
        # проверкa, что есть форма регистрации на странице
         assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Error in REGISTER FORM"