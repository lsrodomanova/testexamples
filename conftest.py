# project/conftest.py
import pytest
from pages.login_page_shop import LoginPage



@pytest.fixture
def login_page_shop(page):
    return LoginPage(page)
