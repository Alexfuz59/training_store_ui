import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Shopping cart")
class TestShoppingCart(BaseTest):

    @allure.title("Home button check")
    def test_home_button(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.open_windows_view_cart()
        self.catalog_page.open_shopping_cart()
        self.shopping_cart_page.button_home_click()
        self.catalog_page.is_opened()

    @allure.title("Checking the start button in an empty shopping cart")
    def test_empty_cart(self):
        self.shopping_cart_page.open()
        self.shopping_cart_page.is_opened()
        self.shopping_cart_page.button_empty_cart_click()
        self.catalog_page.is_opened()

    @allure.title("Checking continue shopping button")
    def test_continue_shopping(self, add_product_to_cart):
        self.shopping_cart_page.is_opened()
        self.shopping_cart_page.button_continue_shopping_click()
        self.catalog_page.is_opened()

    @allure.title("Delete all items from the cart")
    def test_delete_all_cart(self, add_product_to_cart):
        self.shopping_cart_page.is_opened()
        self.shopping_cart_page.button_delete_all_product_click()
        self.shopping_cart_page.check_delete_all_items()

    @allure.title("Delete item from cart")
    def test_delete_items(self, add_product_to_cart):
        self.shopping_cart_page.is_opened()
        total_items = self.shopping_cart_page.items_in_cart()
        self.shopping_cart_page.button_delete_item_product_click()
        self.shopping_cart_page.check_delete_items(total_items)

    @allure.title("Proceed to checkout")
    @pytest.mark.smoke
    def test_proceed_to_checkout(self, add_product_to_cart):
        self.shopping_cart_page.is_opened()
        self.shopping_cart_page.button_proceed_to_checkout_click()
        self.payment_page.current_url_payment()

    @allure.title("Transfer total price from cart to payment")
    @pytest.mark.smoke
    def test_transfer_price_cart_in_payment(self, add_product_to_cart):
        price_cart = self.shopping_cart_page.sum_total_cart()
        self.shopping_cart_page.button_proceed_to_checkout_click()
        self.payment_page.check_sum_total_payment(price_cart)





