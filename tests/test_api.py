import os
from playwright.sync_api import sync_playwright
import allure

@allure.feature('Создание товара')
@allure.story('Создание платья')
@allure.title('Создание аозай')
def test_create_item():
    with sync_playwright() as p:
        # Это запустит новый браузер, создаст контекст и страницу. При выполнении HTTP
        # запросов с использованием внутреннего APIRequestContext (например, `context.request` или `page.request`)
        # cookies будут автоматически установлены на странице браузера и наоборот.
        #browser = p.chromium.launch()
        #context = browser.new_context()
        #api_request_context = context.request
        #page = context.new_page()

        # В качестве альтернативы вы можете создать APIRequestContext вручную без привязки к контексту браузера:
        api_request_context = p.request.new_context(base_url="http://shop.bugred.ru")

        # Создать товар.
        response = api_request_context.post(
            "/api/items/create/",
            data={
        "name":"Аозай красный",
        "section":"Платья",
        "description":"Аозай модный",
        "color":"BLUE",
        "size":46,
        "price":4500,
        "params":"dress"
    },
        )
    assert response.ok
