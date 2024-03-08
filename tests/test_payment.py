import allure
from base.base_test import BaseTest


@allure.feature("Order payment")
class TestPayment(BaseTest):

    @allure.title("Go back to the store")
    def test_back_to_store(self, proceed_to_payment):
        self.payment_page.button_back()
        self.payment_page.button_start_shopping()
        self.catalog_page.is_opened()

