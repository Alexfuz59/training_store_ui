import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Product catalog")
class TestCatalogPrice(BaseTest):

    @allure.title("Sorting in ascending order")
    def test_sort_asc(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_sorting_click()
        self.catalog_page.button_asc_click()
        self.catalog_page.check_sort_asc()

    @allure.title("Sorting in descending order")
    def test_sort_desc(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_sorting_click()
        self.catalog_page.button_desc_click()
        self.catalog_page.check_sort_desc()

    @allure.title("Show 12 products per page")
    def test_show12(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_show_click()
        self.catalog_page.button_show24_click()
        self.catalog_page.button_show_click()
        self.catalog_page.button_show12_click()
        self.catalog_page.check_quantity_goods(12)

    @allure.title("Show 24 products per page")
    def test_show24(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_show_click()
        self.catalog_page.button_show24_click()
        self.catalog_page.check_quantity_goods(24)

    @allure.title("Show 36 products per page")
    def test_show36(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_show_click()
        self.catalog_page.button_show36_click()
        self.catalog_page.check_quantity_goods(36)

    @allure.title("Showing items from category Electronics")
    def test_categories_electronics(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_categories_click()
        self.catalog_page.button_electronics_click()
        self.catalog_page.check_category()

    @allure.title("Showing items from category Jewelery")
    def test_categories_jewelery(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_categories_click()
        self.catalog_page.button_jewelery_click()
        self.catalog_page.check_category()

    @allure.title("Showing items from category Men clothing")
    def test_categories_men_clothing(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_categories_click()
        self.catalog_page.button_men_clothing_click()
        self.catalog_page.check_category()

    @allure.title("Showing items from category Women clothing")
    def test_categories_women_clothing(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_categories_click()
        self.catalog_page.button_women_clothing_click()
        self.catalog_page.check_category()

    @allure.title("Show items in the list view")
    def test_view_list_catalog(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_view_list_click()
        self.catalog_page.check_view_grid(1)

    @allure.title("Show items in a grid of 3")
    def test_view_grid_catalog_3product(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_view_list_click()
        self.catalog_page.button_view_grid_3products_click()
        self.catalog_page.check_view_grid(3)

    @allure.title("Show items in a grid of 4")
    def test_view_grid_catalog_4product(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.button_view_grid_4products_click()
        self.catalog_page.check_view_grid(4)

    @allure.title("Add item to cart")
    @pytest.mark.smoke
    @pytest.mark.parametrize('quantityAdd', [1, 2, 10])
    def test_add_item_to_cart(self, quantityAdd):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.add_item_to_cart(quantityAdd)
        self.catalog_page.open_windows_view_cart()
        self.catalog_page.open_shopping_cart()
        productCarte = self.shopping_cart_page.quantity_total_product_in_cart()
        self.catalog_page.check_items_in_cart(productCarte, quantityAdd)

    @allure.title("Clear cart in the cart view window")
    def test_delete_item_from_windows_view_cart(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.catalog_page.add_item_to_cart()
        self.catalog_page.open_windows_view_cart()
        self.catalog_page.button_delete_items()
        productCarte = self.shopping_cart_page.quantity_total_product_in_cart()
        self.catalog_page.check_items_in_cart(productCarte)

    @allure.title("Open order history")
    def test_open_histore_orders(self):
        self.catalog_page.open()
        self.catalog_page.is_opened()
        self.orders_page.open_orders_history()
        self.orders_page.is_opened()






