import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC


class BasePage:

    BUTTON_HOME_SELECTOR = ('xpath', '//a[@routerlink="home"]')
    BUTTON_ORDERS_SELECTOR = ('xpath', '//button[@routerlink="orders"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 8, poll_frequency=1)
        self.action = AC(driver)

    @allure.step('Open URL')
    def open(self):
        self.driver.get(self.PAGE_URL)

    @allure.step('Check is opened URL')
    def is_opened(self):
        try:
            self.wait.until(EC.url_to_be(self.PAGE_URL))
        except TimeoutException:
            raise TimeoutException("Wrong page opened")

    @allure.step('Click button home')
    def button_home_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_HOME_SELECTOR)).click()

    @allure.step('Open order history')
    def open_orders_history(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ORDERS_SELECTOR)).click()

    @allure.step('Refresh page')
    def refresh(self):
        self.driver.refresh()


