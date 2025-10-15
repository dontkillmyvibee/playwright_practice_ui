import allure
import pytest
from _pytest.fixtures import SubRequest

from playwright.sync_api import Page, Playwright

from config import settings


@pytest.fixture(params=settings.browsers)
def page(request: SubRequest, playwright: Playwright) -> Page:
    browser_type=request.param
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(record_video_dir=settings.videos_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{request.node.name}.zip'))
    browser.close()

    allure.attach.file(settings.tracing_dir.joinpath(f'{request.node.name}.zip'), name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

