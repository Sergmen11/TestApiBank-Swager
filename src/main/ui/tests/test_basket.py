from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.basket_steps import BasketSteps
from src.main.ui.steps.checkout_steps import CheckoutSteps


def test_add_item_and_check_in_cart(page):
    basket = BasketSteps(page)
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")

    # добавляем Sauce Labs Backpack
    catalog.add_product_in_cart("Sauce Labs Backpack")

    # переходим в корзину
    basket.open_basket()

    # проверяем что товар добавился в корзину
    basket.expect_item_in_cart("Sauce Labs Backpack"), "Товар не добавился в корзину"

def test_add_items_and_check_in_cart(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    basket = BasketSteps(page)

    # добавляем Sauce Labs Fleece Jacket and Sauce Labs Bolt T-Shirt
    catalog.add_product_in_cart("Sauce Labs Fleece Jacket")
    catalog.add_product_in_cart("Sauce Labs Bolt T-Shirt")

    # переходим в корзину
    basket.open_basket()

    # проверяем, что товар действительно добавился в корзину
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket"), "Товар не добавился в корзину"
    basket.expect_item_in_cart("Sauce Labs Bolt T-Shirt"), "Товар не добавился в корзину"

def test_remove_item_from_cart(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    catalog.login("standard_user", "secret_sauce")

    # добавляем товар в корзину
    catalog.add_product_in_cart("Sauce Labs Fleece Jacket")

    # переходим в корзину
    basket.open_basket()

    # удаляем товар
    basket.remove_item_from_cart("Sauce Labs Fleece Jacket")

    # проверяем что товар удалился из корзины
    basket.expect_item_not_in_cart("Sauce Labs Fleece Jacket"), "Товар не удалился из корзины"

def test_remove_items_from_cart(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    basket = BasketSteps(page)

    # добавляем товар в корзину
    catalog.add_product_in_cart("Sauce Labs Fleece Jacket")
    catalog.add_product_in_cart("Sauce Labs Bolt T-Shirt")

    # переходим в корзину
    basket.open_basket()

    # проверяем, что товар действительно добавился в корзину
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket"), "Товар не добавился в корзину"
    basket.expect_item_in_cart("Sauce Labs Bolt T-Shirt"), "Товар не добавился в корзину"

    # удаляем товар
    basket.remove_item_from_cart("Sauce Labs Fleece Jacket")
    basket.remove_item_from_cart("Sauce Labs Bolt T-Shirt")

    # проверяем что товар удален из корзины
    basket.expect_item_not_in_cart("Sauce Labs Fleece Jacket"), "Товар не удалился из корзины"
    basket.expect_item_not_in_cart("Sauce Labs Bolt T-Shirt"), "Товар не удалился из корзины"

def test_checkout_multiple_items(page):
    catalog = CatalogSteps(page)
    catalog.login("standard_user", "secret_sauce")
    basket = BasketSteps(page)

    # добавляем Sauce Labs Fleece Jacket and Sauce Labs Bolt T-Shirt
    catalog.add_product_in_cart("Sauce Labs Fleece Jacket")
    catalog.add_product_in_cart("Sauce Labs Bolt T-Shirt")

    # переходим в корзину
    basket.open_basket()

    # проверяем, что товар действительно добавился в корзину
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket"), "Товар не добавился в корзину"
    basket.expect_item_in_cart("Sauce Labs Bolt T-Shirt"), "Товар не добавился в корзину"

    # Считаем сумму корзины перед чекаутом
    basket_total = basket.get_items_total_price()

    # переходим к оформлению товару
    basket.open_checkout()

    # заполнение карточки для заказа товара
    checkout = CheckoutSteps(page)
    checkout.fill_checkout_form("Sergey", "Ivanov", "344409")

    # проверяем сумму заказа
    assert basket_total == checkout.get_total_price(), "Суммы заказа не совпадают"

    # кликаем на кнопку завершить заказ (Finish)
    checkout.finish_checkout()

    # проверка, что появилась надпись об удачном заказе
    checkout.expect_success_message(), "Не появилась надпись об удачном заказе"

def test_checkout_without_items(page):
    catalog = CatalogSteps(page)
    basket = BasketSteps(page)
    checkout = CheckoutSteps(page)

    catalog.login("standard_user", "secret_sauce")

    # Добавляем товар
    catalog.add_product_in_cart("Sauce Labs Fleece Jacket")

    # Переход в корзину
    basket.open_basket()

    # Проверяем что товар добавлен в корзину
    basket.expect_item_in_cart("Sauce Labs Fleece Jacket")

    # Жмем Checkout
    basket.open_checkout()

    # Заполняем поле First Name и Last Name и жмем Continue
    checkout.fill_checkout_form("Sergey", "Ivanov", "")

    # Проверяем ошибку
    checkout.expect_error_message(), "Ожидалась ошибка при оформлении пустой корзины"