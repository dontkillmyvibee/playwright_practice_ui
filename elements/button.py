from playwright.sync_api import Page, expect

from elements.base_element import BaseElement


class Button(BaseElement):

    def check_enabled(self):
        locator = self.get_locator()
        expect(locator).to_be_enabled()

    def check_disabled(self):
        locator = self.get_locator()
        expect(locator).to_be_disabled()
