import pytest

from playwright.sync_api import Page

from pages.authentication_page import AuthenticationPage


@pytest.fixture
def auth_page(page: Page) -> AuthenticationPage:
    return AuthenticationPage(page=page)
