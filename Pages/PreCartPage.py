from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class PreCartPage(BasePage):

    cart_overview_btn = (By.LINK_TEXT, "Pārlūkot pirkumu grozu")

    def __int__(self, driver):
        super().__init__(driver)

    def click_on_cart_overview(self):
        self.click_on(self.cart_overview_btn)

