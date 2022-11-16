import time
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.keys import Keys


class ListPage(BasePage):

    href_value = TestData.PRODUCT
    partial_link_product = (By.PARTIAL_LINK_TEXT, TestData.PRODUCT)

    def __int__(self, driver):
        super().__init__(driver)

    # couldn't click properly, customized to have Key action :(
    def click_on_product(self):
        body = self.driver.find_element(By.CSS_SELECTOR, "body")
        body.send_keys(Keys.PAGE_DOWN)
        self.click_on(self.partial_link_product)

    # not smart workaround! :)
    # a = self.listPage.get_href_attribute()
    # self.driver.get(a)
    def get_href_attribute(self):
        time.sleep(2)
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.href_value)
        print(element.get_attribute('href'))
        return element.get_attribute('href')
