from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        self.should_be_button_add_to_basket()
        self.should_be_correct_messages_about_add_product_to_backet()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_BASKET), "Button ADD TO BASKET is unavailable"

    def should_be_correct_messages_about_add_product_to_backet(self):
        button1 = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        button1.click()
        self.solve_quiz_and_get_code()
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Messages about add product to backetis are not present"

        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        #print(product.text)
        #print(product_in_message.text)
        assert product.text == product_in_message.text, "Error in name product"
        
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        price_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)
        #print(price.text)
        #print(price_in_message.text)
        assert price.text == price_in_message.text, "Error in price product"
        



# Ожидаемый результат: 
# Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
# Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 