from elements.base_element import BaseElement


class FileInput(BaseElement):
    def set_input_files(self, file_path: str):
        locator = self.get_locator()
        locator.set_input_files(file_path)