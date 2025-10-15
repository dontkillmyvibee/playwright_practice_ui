import allure
from playwright.sync_api import Page, expect

from elements.base_element import BaseElement


class Button(BaseElement):
    @property
    def type_of(self):
        return 'button'

    def check_enabled(self):
        locator = self.get_locator()
        step = f'Checking that {self.type_of} "{self.name}" is enabled.'
        with allure.step(step):
            expect(locator).to_be_enabled()

    def check_disabled(self):
        locator = self.get_locator()
        step = f'Checking that {self.type_of} "{self.name}" is disabled.'
        with allure.step(step):
            expect(locator).to_be_disabled()
