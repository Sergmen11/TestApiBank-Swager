from playwright.sync_api import Page
from src.main.ui.utils.constants import Urls


class CheckoutPage:
    URL = Urls.CHECKOUT
    def __init__(self, page: Page):
        self.page = page
        self.input_first_name = page.get_by_placeholder("First name")
        self.input_last_name = page.get_by_placeholder("Last name")
        self.input_postal_code = page.get_by_placeholder("Zip/Postal code")
        self.button_continue = page.get_by_role("button", name="Continue")
        self.item_total = page.locator('.summary_subtotal_label')
        self.button_finish = page.get_by_role("button", name="finish")
        self.error_message = page.locator('[data-test="error"]')
        self.success_message = page.locator(".complete-header")

    def finish_checkout(self):
        self.button_finish.click()

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.input_first_name.fill(first_name)
        self.input_last_name.fill(last_name)
        self.input_postal_code.fill(postal_code)
        self.button_continue.click()

    def get_total_price(self) -> float:
        text_total = self.item_total.inner_text()
        return float(text_total.split('$')[1])

    def get_error_message(self) -> str:
        return self.error_message.inner_text()

    def get_success_message(self) -> str:
        return self.success_message.inner_text()

    def expect_success_message(self):
        assert self.get_success_message() == "Thank you for your order!"

    def invalid_fill_checkout_form(self, first_name: str, last_name: str):
        self.input_first_name.fill(first_name)
        self.input_last_name.fill(last_name)
        self.button_continue.click()

    def expect_error_message(self):
        assert self.get_error_message() == "Error: Postal Code is required"