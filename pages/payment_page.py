import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage(BasePage):
    SUM_TOTAL_PAYMENT_SELECTOR = ('xpath', '(//span[@class="CurrencyAmount"])[4]',)
    BUTTON_BACK_SELECTOR = ('xpath', '//a[contains(@href, "http://16.170.215.221:9090/web/stripe/payment/cancel.html")]')
    BUTTON_START_SHOPPING_SELECTOR = ('xpath', '//button[text()="Start shopping"]',)

    @allure.step("Checking the final price in payment")
    def check_sum_total_payment(self, price_cart):
        price_cart = price_cart.strip('$').strip()
        price_payment = self.wait.until(EC.presence_of_element_located(self.SUM_TOTAL_PAYMENT_SELECTOR)).text
        price_payment = price_payment.strip('$').strip().replace(',', '.')
        assert float(price_payment) == float(price_cart), "Total price in payment does not match the cart"

    @allure.step("Checking the site domain")
    def current_url_payment(self):
        self.wait.until(EC.url_contains('checkout.stripe.com'))

    @allure.step("Click the back button")
    def button_back(self):
        button_back = self.wait.until(EC.element_to_be_clickable(self.BUTTON_BACK_SELECTOR))
        self.action.move_to_element(button_back) \
            .pause(1) \
            .click() \
            .perform()

    @allure.step("Click the start shopping button")
    def button_start_shopping(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_START_SHOPPING_SELECTOR)).click()


