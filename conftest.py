import pytest
import allure
import selenium.webdriver.firefox.service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_firefox
from pages.catalog_page import CatalogPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.payment_page import PaymentPage
from config.environment_allure import EnvironmentAllure


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    browser_name = request.config.getoption("browser_name")
    EnvironmentAllure.create_environment(browser_name)
    if browser_name == "chrome":
        options_chrome = Options_chrome()
        options_chrome.add_argument("--headless")
        options_chrome.add_argument("--disable-cache")
        options_chrome.add_argument('--ignore-certificate-errors')
        print("\nstart Chrome browser for test..")
        driver = webdriver.Chrome(options=options_chrome)
        request.cls.driver = driver
    elif browser_name == "firefox":
        options_firefox = Options_firefox()
        firefox_bin = "/snap/firefox/current/usr/lib/firefox/firefox"
        firefoxdriver_bin = "/snap/firefox/current/usr/lib/firefox/geckodriver"
        options_firefox.binary_location = firefox_bin
        options_firefox.add_argument("--headless")
        options_firefox.add_argument("--disable-cache")
        options_firefox.add_argument('--ignore-certificate-errors')
        service = selenium.webdriver.firefox.service.Service(executable_path=firefoxdriver_bin)
        print("\nstart Firefox browser for test..")
        driver = webdriver.Firefox(service=service, options=options_firefox)
        request.cls.driver = driver
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()


@allure.title("Add item to cart")
@pytest.fixture()
def add_product_to_cart(driver):
    catalog_page = CatalogPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)
    catalog_page.open()
    catalog_page.is_opened()
    catalog_page.add_item_to_cart()
    catalog_page.open_windows_view_cart()
    catalog_page.open_shopping_cart()
    shopping_cart_page.is_opened()


@allure.title("Go to payment")
@pytest.fixture()
def proceed_to_payment(driver, add_product_to_cart):
    shopping_cart_page = ShoppingCartPage(driver)
    payment_page = PaymentPage(driver)
    shopping_cart_page.button_proceed_to_checkout_click()
    payment_page.current_url_payment()
