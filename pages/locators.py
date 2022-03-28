from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():  
    BTN_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "div#messages")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".product_main p.price_color")
    

