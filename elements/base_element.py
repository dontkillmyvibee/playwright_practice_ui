from playwright.sync_api import Page, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self):
        locator = self.locator
        return self.page.locator(locator)

    def click(self):
        locator = self.get_locator()
        locator.click()

    def check_visible(self):
        locator = self.get_locator()
        expect(locator).to_be_visible()

    def check_have_text(self, text: str):
        locator = self.get_locator()
        expect(locator).to_have_text(text)

    def check_attribute(self, name_attribute: str, key_attribute: str):
        locator = self.get_locator()
        expect(locator).to_have_attribute(name_attribute, key_attribute)
