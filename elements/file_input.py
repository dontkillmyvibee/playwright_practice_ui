import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self):
        return 'file input'

    def set_input_files(self, file_path: str):
        locator = self.get_locator()
        step = f'Uploading "{file_path}" to {self.type_of} "{self.name}".'
        with allure.step(step):
            locator.set_input_files(file_path)