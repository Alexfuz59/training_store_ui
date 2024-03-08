import random
import allure
import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage(BasePage):
    PAGE_URL = Links.CATALOG_PAGE
    BUTTON_SELECTOR_SORTING = ('xpath', '//button[@class="mat-focus-indicator mat-menu-trigger mat-button mat-button-base"][1]')
    BUTTON_SELECTOR_ASC = ('xpath', '//button[@role="menuitem"][2]')
    BUTTON_SELECTOR_DESC = ('xpath', '//button[@role="menuitem"][1]')
    LIST_ELEMENTS_SELECTOR_PRICE = ('xpath', '//span[@class="text-red-400"]',)
    BUTTON_SHOW = ('xpath', '(//button[contains(@class, "mat-focus-indicator")])[4]')
    BUTTON_SHOW12 = ('xpath', '(//button[contains(@class, "mat-focus-indicator")])[5]')
    BUTTON_SHOW24 = ('xpath', '(//button[contains(@class, "mat-focus-indicator")])[6]')
    BUTTON_SHOW36 = ('xpath', '(//button[contains(@class, "mat-focus-indicator")])[7]')
    BUTTON_ELECTRONICS_SELECTOR = ('xpath', '(//mat-list-option[contains(@role, "option")])[1]')
    BUTTON_JEWELERY_SELECTOR = ('xpath', '(//div[contains(@class, "mat-list-item-content")])[2]')
    BUTTON_MEN_CLOTHING_SELECTOR = ('xpath', '(//div[contains(@class, "mat-list-item-content")])[3]')
    BUTTON_WOMEN_CLOTHING_SELECTOR = ('xpath', '(//div[contains(@class, "mat-list-item-content")])[4]')
    BUTTON_CATEGORIES_SELECTOR = ('xpath', '//mat-panel-title[contains(@class, "mat-expansion-panel-header-title")]')
    LIST_ELEMENTS_CATEGORIES_SELECTOR = ('xpath', '//h5')
    BUTTON_VIEW_LIST_SELECTOR = ('xpath', '(//mat-icon[contains(@class, "mat-ligature-font")])[5]')
    BUTTON_VIEW_GRID3_SELECTOR = ('xpath', '(//mat-icon[contains(@class, "mat-ligature-font")])[6]')
    BUTTON_VIEW_GRID4_SELECTOR = ('xpath', '(//mat-icon[contains(@class, "mat-ligature-font")])[7]')
    GRID_LIST_SELECTOR = ('xpath', '//mat-grid-list[@guttersize="16"]')
    ADD_ITEM_CART_SELECTOR = ('xpath', '//mat-icon[contains(@class, "text-gray-500")]')
    WINDOWS_VIEW_CART_SELECTOR = ('xpath', '(//mat-icon[text()="shopping_cart"])[1]')
    OPEN_SHOPPING_CART = ('xpath', '//button[@routerlink="cart"]')
    BUTTON_DELETE_ITEM_SELECTOR = ('xpath', '//button[contains(@class, "bg-rose-600")]')
    ELEMENTS_SELECTOR_PRICE = ('xpath', '(//span[@class="text-red-400"])[1]',)
    BUTTON_CATEGORIES_TRUE_SELECTOR = ('xpath', '//mat-list-option[@aria-selected="true"]')
    BUTTON_POP_UP_WINDOW_SELECTOR = ('xpath', '//snack-bar-container')

    @allure.step("Click the sort button")
    def button_sorting_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SELECTOR_SORTING)).click()

    @allure.step("Click the sort in ascending order button")
    def button_asc_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SELECTOR_ASC)).click()

    @allure.step("Click the sort by descending button")
    def button_desc_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SELECTOR_DESC)).click()

    @allure.step("Generate list of prices")
    def list_price(self):
        list_price = []
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.ELEMENTS_SELECTOR_PRICE))
        for element in self.driver.find_elements(*self.LIST_ELEMENTS_SELECTOR_PRICE):
            list_price.append(element.text)
        return list_price

    @allure.step("Click the show button")
    def button_show_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SHOW)).click()

    @allure.step("Click button show by 12")
    def button_show12_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SHOW12)).click()

    @allure.step("Click button show by 24")
    def button_show24_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SHOW24)).click()

    @allure.step("Click button show by 36")
    def button_show36_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_SHOW36)).click()

    @allure.step("Click the Categories button")
    def button_categories_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_CATEGORIES_SELECTOR)).click()

    @allure.step("Click the Electronics button")
    def button_electronics_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ELECTRONICS_SELECTOR)).click()
        self.wait.until(EC.presence_of_element_located(self.BUTTON_CATEGORIES_TRUE_SELECTOR))

    @allure.step("Click the Jewelery button")
    def button_jewelery_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_JEWELERY_SELECTOR)).click()
        self.wait.until(EC.presence_of_element_located(self.BUTTON_CATEGORIES_TRUE_SELECTOR))

    @allure.step("Click the Men clothing button")
    def button_men_clothing_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_MEN_CLOTHING_SELECTOR)).click()
        self.wait.until(EC.presence_of_element_located(self.BUTTON_CATEGORIES_TRUE_SELECTOR))

    @allure.step("Click the Women clothing button")
    def button_women_clothing_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_WOMEN_CLOTHING_SELECTOR)).click()
        self.wait.until(EC.presence_of_element_located(self.BUTTON_CATEGORIES_TRUE_SELECTOR))

    @allure.step("Check product category")
    def categories_test(self):
        list_categories = set()
        time.sleep(2)
        for element in self.driver.find_elements(*self.LIST_ELEMENTS_CATEGORIES_SELECTOR):
            list_categories.add(element.text)
        return list_categories

    @allure.step("Click button view list")
    def button_view_list_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_VIEW_LIST_SELECTOR)).click()

    @allure.step("Click button view grid 3 products")
    def button_view_grid_3products_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_VIEW_GRID3_SELECTOR)).click()

    @allure.step("Click button view grid 4 products")
    def button_view_grid_4products_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_VIEW_GRID4_SELECTOR)).click()

    @allure.step("Checking the grid of the catalog sheet ")
    def attribute_cols_value_gridlist(self):
        return int(self.driver.find_element(*self.GRID_LIST_SELECTOR).get_attribute("cols"))

    @allure.step('Add items to cart')
    def add_item_to_cart(self, quantity=1):
        self.wait.until(EC.presence_of_element_located(self.ADD_ITEM_CART_SELECTOR))
        for i in range(quantity):
            amount_of_elem = len(self.driver.find_elements(*self.ADD_ITEM_CART_SELECTOR))
            number_item = random.randrange(1, amount_of_elem)
            random_product_selector = ('xpath', f'(//mat-icon[contains(@class, "text-gray-500")])[{number_item}]')
            self.wait.until(EC.element_to_be_clickable(random_product_selector)).click()
            self.wait.until(EC.visibility_of_element_located(self.BUTTON_POP_UP_WINDOW_SELECTOR))
            self.wait.until(EC.invisibility_of_element_located(self.BUTTON_POP_UP_WINDOW_SELECTOR))

    @allure.step("Open the cart view window")
    def open_windows_view_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.WINDOWS_VIEW_CART_SELECTOR)).click()

    @allure.step("Open shopping cart")
    def open_shopping_cart(self):
        self.wait.until(EC.presence_of_element_located(self.OPEN_SHOPPING_CART)).click()

    @allure.step("Click delete item")
    def button_delete_items(self):
        self.wait.until(EC.presence_of_element_located(self.BUTTON_DELETE_ITEM_SELECTOR)).click()

    @allure.step("Check sorting by ascending")
    def check_sort_asc(self):
        assert self.list_price() == sorted(self.list_price()), 'Error sorting by ascending'

    @allure.step("Check sorting by descending")
    def check_sort_desc(self):
        assert self.list_price() == sorted(self.list_price(), reverse=True),\
            'Error sorting by descending'

    @allure.step("Checking the number of products per page")
    def check_quantity_goods(self, quantity):
        assert len(self.list_price()) == quantity, f'Error, items on the page: {len(self.list_price())}'

    @allure.step("Check product category")
    def check_category(self):
        assert len(self.categories_test()) == 1, 'Error, wrong product category'

    @allure.step("Check product display view")
    def check_view_grid(self, grid):
        assert self.attribute_cols_value_gridlist() == grid, 'Wrong product display grid'

    @allure.step("Checking items in the shopping cart")
    def check_items_in_cart(self, productCarte, quantityAdd=0):
        if productCarte == '':
            productCarte = 0
        assert int(productCarte) == quantityAdd, "Invalid quantity of goods in the store cart"
