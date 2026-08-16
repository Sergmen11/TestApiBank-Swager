from src.main.ui.pages.checkout_page import CheckoutPage
import allure
from playwright.sync_api import Page


class CheckoutSteps:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_page = CheckoutPage(page)

    @allure.step("Заполняем карточку товара")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        self.checkout_page.fill_checkout_form(first_name, last_name, postal_code)
        return self

    @allure.step("Получаем итоговую сумму заказа")
    def get_total_price(self):
        return self.checkout_page.get_total_price()

    @allure.step("Завершаем оформление заказа")
    def finish_checkout(self):
        self.checkout_page.finish_checkout()
        return self

    @allure.step("Проверяем, что появилась надпись об удачном заказе")
    def expect_success_message(self):
        self.checkout_page.expect_success_message()
        return self

    @allure.step("Проверяем, что появилась надпись об ошибке")
    def expect_error_message(self):
        self.checkout_page.expect_error_message()
        return self