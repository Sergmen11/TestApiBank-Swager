from src.main.ui.pages.basket_page import BasketPage
from playwright.sync_api import Page
import allure


class BasketSteps:
    def __init__(self, page: Page):
        self.page = page
        self.basket_page = BasketPage(page)

    @allure.step("Открываем корзину")
    def open_basket(self):
        self.basket_page.open_basket()
        return self

    @allure.step("Проверяем наличие товара в корзине")
    def expect_item_in_cart(self, product_name: str):
        self.basket_page.expect_item_in_cart(product_name)
        return self

    @allure.step("Удаляем товар из корзины")
    def remove_item_from_cart(self, product_name: str):
        self.basket_page.remove_item_from_cart(product_name)
        return self

    @allure.step("Проверяем, что товар удален из корзины")
    def expect_item_not_in_cart(self, product_name: str):
        self.basket_page.expect_remove_item_from_cart(product_name)
        return self

    @allure.step("Получаем сумму корзины перед чекаутом")
    def get_items_total_price(self) -> float:
        return self.basket_page.get_items_total_price()

    @allure.step("Переходим на страницу чекаута")
    def open_checkout(self):
        self.basket_page.open_checkout()
        return self