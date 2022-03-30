from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        button.click()
  
    def should_be_correct_message_about_name_product(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), "Message about adding product in backet is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE), "Product name is not presented"
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert product.text == product_in_message.text, "Error in name product"
        
    def should_be_correct_message_about_price_product(self):    
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), "Message about total prace in backet is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE), "Product prise is not presented"
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        assert price.text == price_in_message.text, "Error in price product"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
       "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
       "Success message is presented, but should not be"   
                
    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
       "Success message is not disappeared, but should be"