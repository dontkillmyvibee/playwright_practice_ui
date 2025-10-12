from elements.base_element import BaseElement


class TextArea(BaseElement):
    def fill(self, value):
        locator = self.get_locator()
        locator.fill(value)

    def check_have_value(self, value):
        locator = self.get_locator()
        locator.check_have_value(value)


