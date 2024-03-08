import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage(BasePage):
    PAGE_URL = Links.SHOPPING_CART
    QUANTITY_TOTAL_PRODUCT_SELECTOR = ('xpath', '//span[@id="mat-badge-content-0"]')
    BUTTON_EMPTY_CART_SELECT = ('xpath', '//button[@routerlink="/home"]')
    BUTTON_DELETE_ALL_PRODUCT_SELECT = ('xpath', '(//button[@color="warn"])[1]')
    BUTTON_DELETE_ITEM_PRODUCT_SELECT = ('xpath', '(//button[@color="warn"])[2]')
    BUTTON_CONTINUE_SHOPPING_SELECT = ('xpath', '//button[@routerlink="/home"]')
    BUTTON_PROCEED_TO_CHECKOUT_SELECT = ('xpath', '//button[@color="primary"]')
    ITEMS_IN_CART_SELECTOR = ('xpath', '//tr[contains(@class, "mat-row")]')
    SUM_TOTAL_CART_SELECTOR = ('xpath', '//span[@class="font-bold py-5 block"]')

    @allure.step("Show the number of products in the shopping cart")
    def quantity_total_product_in_cart(self):
        return self.driver.find_element(*self.QUANTITY_TOTAL_PRODUCT_SELECTOR).text

    @allure.step("Click the button to start shopping")
    def button_empty_cart_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_EMPTY_CART_SELECT)).click()

    @allure.step("Click the delete all products button")
    def button_delete_all_product_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_DELETE_ALL_PRODUCT_SELECT)).click()

    @allure.step("Click to delete the product")
    def button_delete_item_product_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_DELETE_ITEM_PRODUCT_SELECT)).click()

    @allure.step("Click the Continue Shopping button")
    def button_continue_shopping_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CONTINUE_SHOPPING_SELECT)).click()

    @allure.step("Number of items in cart")
    def items_in_cart(self):
        return len(self.driver.find_elements(*self.ITEMS_IN_CART_SELECTOR))

    @allure.step("Click the payment button")
    def button_proceed_to_checkout_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_PROCEED_TO_CHECKOUT_SELECT)).click()

    @allure.step("Total price in cart")
    def sum_total_cart(self):
        return self.driver.find_element(*self.SUM_TOTAL_CART_SELECTOR).text

    @allure.step("Checking the deletion of all items")
    def check_delete_all_items(self):
        assert self.items_in_cart() == 0, "All items are not deleted from the cart"

    @allure.step("Checking the deleted item")
    def check_delete_items(self, before_delete):
        assert self.items_in_cart() == before_delete - 1, "The item has not been removed from the cart"
