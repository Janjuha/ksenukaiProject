from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ProductPage(BasePage):

    add_to_cart_btn = (By.ID, "add_to_cart_btn")
    quantity_field = (By.ID, "product_quantity")
    increase_button = (By.ID, "inc-quantity")

    def __int__(self, driver):
        super().__init__(driver)

    def send_keys_quantity(self, quantity):
        self.clear_and_send_keys(self.quantity_field, quantity)

    def click_put_to_cart(self):
        self.click_on(self.add_to_cart_btn)
