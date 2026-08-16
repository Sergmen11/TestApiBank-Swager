from playwright.sync_api import Page
from src.main.ui.utils.constants import Urls

class LoginPage:
    URL = Urls.BASE
    def __init__(self, page: Page):
        self.page = page
        self.input_username = page.get_by_placeholder("Username")
        self.input_password = page.get_by_placeholder("Password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test=error]")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        return self.error_message.inner_text()