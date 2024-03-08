import pytest
from pages.catalog_page import CatalogPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.orders_page import OrdersHistoryPage
from pages.payment_page import PaymentPage


class BaseTest:

    catalog_page: CatalogPage
    shopping_cart_page: ShoppingCartPage
    orders_page: OrdersHistoryPage
    payment_page: PaymentPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.catalog_page = CatalogPage(driver)
        request.cls.shopping_cart_page = ShoppingCartPage(driver)
        request.cls.orders_page = OrdersHistoryPage(driver)
        request.cls.payment_page = PaymentPage(driver)

