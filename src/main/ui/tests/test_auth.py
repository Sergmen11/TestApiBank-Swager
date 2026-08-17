from src.main.ui.steps.catalog_steps import CatalogSteps
from src.main.ui.steps.login_steps import LoginSteps


def test_auth(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("standard_user", "secret_sauce")

    catalog = CatalogSteps(page)

    # проверяем, что мы на странице каталога
    assert catalog.get_count_products_page_catalog() > 0

def test_login_locked_out_user(page):
    steps = LoginSteps(page)
    steps.open_login_page().login("locked_out_user", "secret_sauce")

    error_text = steps.login_page.get_error_text()
    assert "locked out" in error_text, "Ожидаем сообщение о заблокированном пользователе"

def test_logout(page):
    login = LoginSteps(page)
    login.open_login_page().login("standard_user", "secret_sauce")

    catalog = CatalogSteps(page)

    # Проверяем, что мы на странице каталога
    assert catalog.get_count_products_page_catalog() > 0

    catalog.logaut()
    assert page.url == login.LOGIN_URL, "Ожидаем возврат на страницу логина"

def test_logout_visual_user(page):
    login = LoginSteps(page)
    login.open_login_page().login("visual_user", "secret_sauce")

    catalog = CatalogSteps(page)

    # Проверяем, что мы на странице каталога
    assert catalog.get_count_products_page_catalog() > 0

    # Логаут через Page Object
    catalog.logaut()

    # проверяем возвращение на страницу логина
    assert page.url == login.LOGIN_URL, "Ожидаем возврат на страницу логина"