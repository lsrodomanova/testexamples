import os

import pytest
from playwright.sync_api import sync_playwright
import allure


@pytest.fixture(scope="function")
def create_item():
    with sync_playwright() as p:
        # Это запустит новый браузер, создаст контекст и страницу. При выполнении HTTP
        # запросов с использованием внутреннего APIRequestContext (например, `context.request` или `page.request`)
        # cookies будут автоматически установлены на странице браузера и наоборот.
        # browser = p.chromium.launch()
        # context = browser.new_context()
        # api_request_context = context.request
        # page = context.new_page()

        # В качестве альтернативы вы можете создать APIRequestContext вручную без привязки к контексту браузера:
        api_request_context = p.request.new_context(base_url="http://shop.bugred.ru")

        # Создать товар.
        response = api_request_context.post(
            "/api/items/create/",
            data={
                "name": "Аозай",
                "section": "Платья",
                "description": "Аозай модный",
                "color": "BLUE",
                "size": 46,
                "price": 4500,
                "params": "dress"
            },
        )

        data = response.json()
        item_id = data["result"]["id"]
        return item_id


@allure.feature('Поиск товара')
@allure.story('Поиск по названию')
@allure.title('Поиск аозай')
def test_search_item():
    with sync_playwright() as p:
        # Это запустит новый браузер, создаст контекст и страницу. При выполнении HTTP
        # запросов с использованием внутреннего APIRequestContext (например, `context.request` или `page.request`)
        # cookies будут автоматически установлены на странице браузера и наоборот.
        # browser = p.chromium.launch()
        # context = browser.new_context()
        # api_request_context = context.request
        # page = context.new_page()

        # В качестве альтернативы вы можете создать APIRequestContext вручную без привязки к контексту браузера:
        api_request_context = p.request.new_context(base_url="http://shop.bugred.ru")

        # Найти товар.
        response = api_request_context.post(
            "/api/items/search/",
            headers={
                "Accept": "application/json"
            },
            data={
                "query": "Аозай"
            },
        )
        assert response.ok
        assert response.status == 200

        data = response.json()
        items = data.get("result", [])

        assert any(item["title"] == "Аозай" for item in items), "Товар 'Аозай' не найден"


@allure.feature('Удаление товара')
@allure.story('Удаление товара')
@allure.title('Удаление товара')
def test_delete_item(create_item):
    with sync_playwright() as p:
        api_request_context = p.request.new_context(base_url="http://shop.bugred.ru")

        # Удалить товар.
        response = api_request_context.post(
            "/api/items/delete/",
            data={
                "id": create_item
            },
        )
    assert response.ok
    assert response.status == 200
