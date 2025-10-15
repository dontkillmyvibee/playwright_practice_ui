import allure

from elements.base_element import BaseElement


class TextArea(BaseElement):
    @property
    def type_of(self):
        return 'textarea'

    def fill(self, value):
        locator = self.get_locator()
        step = f'Filling "{value}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
            locator.fill(value)

    def check_have_value(self, value):
        locator = self.get_locator()
        step = f'Checking {self.type_of} "{self.name}" has value "{value}"'
        with allure.step(step):
            locator.check_have_value(value)
