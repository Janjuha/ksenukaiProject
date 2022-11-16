import pytest
from Config.config import TestData
from Pages.CartPage import CartPage
from Pages.ListPage import ListPage
from Pages.MainPage import MainPage
from Pages.ProductPage import ProductPage
from Pages.PreCartPage import PreCartPage


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Ksenukai(BaseTest):

    def test_price(self):
        self.mainPage = MainPage(self.driver)
        self.mainPage.click_on_cookies()
        self.mainPage.search_for_product(TestData.PRODUCT)
        self.listPage = ListPage(self.driver)
        self.listPage.click_on_product()
        self.productPage = ProductPage(self.driver)
        self.productPage.send_keys_quantity(TestData.QUANTITY)
        self.productPage.click_put_to_cart()
        self.preCartPage = PreCartPage(self.driver)
        self.preCartPage.click_on_cart_overview()
        self.cartPage = CartPage(self.driver)
        piece_price = self.cartPage.string_to_number(self.cartPage.get_phone_price())
        final_price = self.cartPage.string_to_number(self.cartPage.get_total_price())
        assert (piece_price * float(TestData.QUANTITY)) == final_price
