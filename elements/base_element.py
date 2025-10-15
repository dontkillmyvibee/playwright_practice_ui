import allure
from playwright.sync_api import Page, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self):
        return 'base element'

    def get_locator(self):
        locator = self.locator
        step = f'Getting locator: "{locator}".'
        with allure.step(step):
            return self.page.locator(locator)

    def click(self):
        step = f'Clicking {self.type_of} "{self.name}".'
        with allure.step(step):
            locator = self.get_locator()
            locator.click()

    def check_visible(self):
        locator = self.get_locator()
        step = f'Checking that {self.type_of} "{self.name}" is visible.'
        with allure.step(step):
            expect(locator).to_be_visible()

    def check_have_text(self, text: str):
        locator = self.get_locator()
        step = f'Checking that {self.type_of} "{self.name}" has text: "{text}".'
        with allure.step(step):
            expect(locator).to_have_text(text)

    def check_attribute(self, name_attribute: str, key_attribute: str):
        locator = self.get_locator()
        step = f'Checking that {self.type_of} "{self.name}" has attribute: "{name_attribute}={key_attribute}".'
        with allure.step(step):
            expect(locator).to_have_attribute(name_attribute, key_attribute)
