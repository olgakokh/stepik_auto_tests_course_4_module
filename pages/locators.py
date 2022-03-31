from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOG_REG_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    LOG_REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    LOG_REG_PASSWORD_DOUBLE = (By.CSS_SELECTOR, "#id_registration-password2")
    LOG_REG_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():  
    BTN_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:first-child strong")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".product_main p.price_color")

class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "content_inner")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#messages")