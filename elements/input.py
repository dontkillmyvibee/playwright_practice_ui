import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self):
        return 'input'

    def fill(self, value: str):
        locator = self.get_locator()
        step = f'Filling "{value}" to {self.type_of} "{self.name}".'
        with allure.step(step):
            locator.fill(value)

    def check_have_value(self, value):
        locator = self.get_locator()
        step = f'Checking that {self.type_of} "{self.name}" has value: "{value}".'
        with allure.step(step):
            expect(locator).to_have_value(value)
