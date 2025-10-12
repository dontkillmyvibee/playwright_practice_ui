from playwright.sync_api import expect

from elements.base_element import BaseElement


class Input(BaseElement):
    def fill(self, value: str):
        locator = self.get_locator()
        locator.fill(value)

    def check_have_value(self, value):
        locator = self.get_locator()
        expect(locator).to_have_value(value)
