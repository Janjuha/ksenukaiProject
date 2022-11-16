import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        # to disable Chrome info bar
        service = Service(TestData.CHROME_EXECUTABLE_REL_PATH)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # to disable Chrome notifications
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(options=chrome_options, service=service)
    if request.param == "firefox":
        options = Options()
        options.binary_location = TestData.FF_BINARY
        driver = webdriver.Firefox(options=options)
    request.cls.driver = driver
    driver.maximize_window()
    driver.get(TestData.BASE_URL)
    yield
    driver.close()
