import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Order history")
class TestOrdersHistory(BaseTest):

    @allure.title("Delete order")
    def test_delete_orders(self, proceed_to_payment):
        self.orders_page.open()
        self.orders_page.is_opened()
        total_orders = self.orders_page.total_orders()
        self.orders_page.delete_first_order()
        self.orders_page.refresh()
        self.orders_page.check_delete_order(total_orders)

    @allure.title("Change order status")
    @pytest.mark.smoke
    def test_update_status_orders(self, proceed_to_payment):
        self.orders_page.open()
        self.orders_page.is_opened()
        status = self.orders_page.status_order()
        self.orders_page.update_status_order()
        self.orders_page.choice_update_status_order()
        self.orders_page.refresh()
        self.orders_page.check_update_status_order(status)
