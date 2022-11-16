import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on(self, by_locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(by_locator)).click()

    def click_on_custom(self, by_locator):
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    # somehow clear() didn't work for input field
    def clear_and_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL, "a")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))
        return self.driver.title
