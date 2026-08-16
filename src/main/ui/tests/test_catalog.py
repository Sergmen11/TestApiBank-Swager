from src.main.ui.steps.catalog_steps import CatalogSteps


def test_count_catalog(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    # проверяем количество товаров
    assert steps.get_count_products_page_catalog() == 6

def test_sorted_by_name(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.sort_items('az')
    assert steps.get_product_names() == sorted(steps.get_product_names()), "Товары не отсортированы по имени A-Z"

    steps.sort_items('za')
    assert steps.get_product_names() == sorted(steps.get_product_names(), reverse=True), "Товары не отсортированы по имени Z-A"

def test_sort_by_price(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.sort_items("lohi")
    assert steps.get_product_prices() == sorted(steps.get_product_prices()), "Товары не отсортированы по цене low -> high"

    steps.sort_items("hilo")
    assert steps.get_product_prices() == sorted(steps.get_product_prices(), reverse=True), "Товары не отсортированы по цене"

def test_add_to_cart(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.add_product_in_cart("Sauce Labs Backpack")
    assert steps.get_cart_count() == 1, "Проверяем что товар добавился в корзину"

def test_add_and_remove_onesie(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.add_product_in_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 1, "Товар не добавлен в корзину"

    steps.remove_product_from_cart("Sauce Labs Onesie")
    assert steps.get_cart_count() == 0, "Товар не удален с корзины"

def test_product_details_onesie(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Onesie")
    assert name == detail_name, "Нет товара в корзине с таким названием"
    assert price == detail_price, "Цена не соотвествует"

def test_product_details_jacket(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    name, price, detail_name, detail_price = steps.open_product_details("Sauce Labs Fleece Jacket")
    # проверяем что название и цену на странице деталей совпадают с названием и цену товара
    assert name == detail_name, "Название товара не совпадает"
    assert price == detail_price, "Цена товара не совпадает"

def test_remove_item_from_catalog(page):
    steps = CatalogSteps(page)
    steps.login("standard_user", "secret_sauce")

    steps.remove_product_from_cart("Test.allTheThings() T-Shirt (Red)")