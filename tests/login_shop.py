import re
# project/tests/test_login.py
import pytest
import allure
from conftest import login_page_shop
from playwright.sync_api import expect, Page



@allure.feature('Авторизация')
@allure.story('Авторизации недействительные учетные данные')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с недействительными учетными данными')
def test_login_failure(login_page_shop):
    with allure.step('Открыть страницу авторизации'):
        login_page_shop.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page_shop.login('invalid_user', 'invalid_password')
    with allure.step('Отображается ошибка - Email пароль неверный!.'):
        expect(login_page_shop.error_message).to_have_text('Email пароль неверный!')


@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('bagovnet@red.ru', '12345678')
])
def test_login_success(username, password, login_page_shop):
    with allure.step('Открыть страницу авторизации'):
        login_page_shop.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page_shop.login(username, password)
    # with allure.step('Отображается личный кабинет с именем пользователя'):
    # expect(login_page_shop.user_profile_button).to_have_text('Lyuba')
    with allure.step('Отображается личный кабинет с именем пользователя'):
        expect(login_page_shop.user_profile_button).to_have_text('Lyuba')
