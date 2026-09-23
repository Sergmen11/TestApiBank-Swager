from playwright.sync_api import Page, expect
from src.main.ui.utils.constants import Urls


class BasketPage:
    URL = Urls.BASE
    def __init__(self, page: Page):
        self.page = page
        self.button_basket = page.locator(".shopping_cart_link")
        self.item_carts = page.locator(".cart_item")
        self.button_checkout = page.locator('[data-test="checkout"]')


    def open_basket(self):
        """Переход в корзину через иконку"""
        self.button_basket.click()

    def open_checkout(self):
        """переход на страницу Checkout"""
        self.button_checkout.click()

    def get_total_prices(self) -> list[float]:
        """Получаем список цен товаров в корзине"""
        prices_text = self.item_carts.locator('.inventory_item_price').all_text_contents()  # получаем список текста по общему классу
        return [float(p.replace("$", "")) for p in prices_text]

    def expect_item_in_cart(self, product_name: str):
        """Проверяем, что товар присутствует в корзине"""
        card = self.item_carts.filter(has_text=product_name)
        expect(card).to_be_visible()

    def remove_item_from_cart(self,product_name: str):
        """Удаляем товар по имени"""
        card = self.item_carts.filter(has_text=product_name)
        button = card.locator("button")
        button.click()

    def expect_remove_item_from_cart(self, product_name: str):
        """Проверяем, что товар отсутствует в корзине"""
        card = self.item_carts.filter(has_text=product_name)
        expect(card).not_to_be_visible()

    def get_items_total_price(self) -> float:
        """Получаем общую стоимость товаров в корзине"""
        return sum(self.get_total_prices())

    def get_name_items(self) -> list[str]:
        """Получаем список названий товаров в корзине"""
        return self.item_carts.locator('.inventory_item_name').all_text_contents()