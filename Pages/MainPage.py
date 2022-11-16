from selenium.webdriver.common.by import By

import Config.config
from Pages.BasePage import BasePage


class MainPage(BasePage):

    search_field = (By.ID, "q")
    search_button = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/form/div/div[2]/button")
    cookies_accept = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")

    def __int__(self, driver):
        super().__init__(driver)

    def get_main_page_title(self):
        return self.get_title()

    def search_for_product(self, product):
        self.send_keys(self.search_field, product)
        self.click_on(self.search_button)

    def click_on_cookies(self):
        self.click_on_custom(self.cookies_accept)

