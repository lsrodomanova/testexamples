import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_reference=page.get_by_role("link", name="Вход")
        self.username_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Пароль")
        self.login_button = page.get_by_role("button", name="Войти")
        self.user_profile_button = page.locator("#navbarDropdown2")
        self.user_account_reference = page.get_by_role("link", name="Личный кабинет")
        self.error_message = page.locator("#alertify")

    def navigate(self):
        """Открывает страницу логина."""
        self.page.goto('http://shop.bugred.ru/', timeout=0)

    def login(self, username: str, password: str):
        """Выполняет вход с заданными учетными данными."""
        self.login_reference.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        """Возвращает текст сообщения об ошибке."""
        return self.error_message.inner_text( timeout=0)

    def check_enter_profile(self, text: str):
        """Проверка, что зашли в личный кабинет"""
        return self.user_profile_button
