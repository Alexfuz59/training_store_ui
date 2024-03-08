import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class OrdersHistoryPage(BasePage):
    PAGE_URL = Links.ORDERS_PAGE
    TOTAL_ORDERS_SELECTOR = ('xpath', '//tr[contains(@class, "mat-row")]')
    DELETE_FIRST_ORDER_SELECTOR = ('xpath', '(//mat-icon[text()="close"])[1]')
    BUTTON_UPDATE_STATUS_ORDER = ('xpath', '(//mat-icon[text()="edit"])[1]')
    BUTTON_CHOICE_UPDATE_STATUS_ORDER = ('xpath', '//button[@role="menuitem"]')
    STATUS_ORDER_BUTTON = ('xpath', '(//tbody/tr/td/span)[1]')

    @allure.step("Total orders in order history")
    def total_orders(self):
        return len(self.driver.find_elements(*self.TOTAL_ORDERS_SELECTOR))

    @allure.step("Delete the first order")
    def delete_first_order(self):
        self.wait.until(EC.element_to_be_clickable(self.DELETE_FIRST_ORDER_SELECTOR)).click()

    @allure.step("Button to change order status")
    def update_status_order(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_UPDATE_STATUS_ORDER)).click()

    @allure.step("Order status change selection button")
    def choice_update_status_order(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CHOICE_UPDATE_STATUS_ORDER)).click()

    @allure.step("Show order status")
    def status_order(self):
        return self.driver.find_element(*self.STATUS_ORDER_BUTTON).text

    @allure.step("Checking changes in order status")
    def check_update_status_order(self, before_status):
        assert before_status != self.status_order(), "Order status has not changed"

    @allure.step("Checking changes to order deletion")
    def check_delete_order(self, before_total):
        assert before_total == self.total_orders() - 1, "Order is not deleted"
