from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CartPage(BasePage):

    price_span_xpath = (By.XPATH, ".//p[@class = 'detailed-cart-item__price']")
    total_price_span_class = (By.CLASS_NAME, "detailed-cart-item__total")

    def __int__(self, driver):
        super().__init__(driver)

    def get_phone_price(self):
        return self.get_text(self.price_span_xpath)

    def get_total_price(self):
        return self.get_text(self.total_price_span_class)

    def string_to_number(self, some_string):
        list_of_chars = ['.', '€', ' ']
        for character in list_of_chars:
            some_string = some_string.replace(character, '')
        return float(some_string.replace(",", "."))
