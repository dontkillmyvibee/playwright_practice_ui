import pytest
from _pytest.fixtures import SubRequest

from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def page(request: SubRequest) -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)

        yield context.new_page()

        context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
        browser.close()
