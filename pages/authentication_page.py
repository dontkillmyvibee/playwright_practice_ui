from components.auth_components.sign_in_form_component import SignInFormComponent
from components.auth_components.sign_up_form_component import SignUpFormComponent
from components.auth_components.user_profile_component import UserProfileComponent
from elements.button import Button
from pages.base_page import BasePage

from playwright.sync_api import Page


class AuthenticationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.url = "https://www.practicetestqa.xyz/authentication"

        self.sign_in_form = SignInFormComponent(page)
        self.sign_up_form = SignUpFormComponent(page)
        self.user_profile_form = UserProfileComponent(page)

        self.sign_in_tab = Button(page, '//button[@id="sign-in-tab"]', 'Sign in tab')
        self.sign_up_tab = Button(page, '//button[@id="sign-up-tab"]', 'Sign up tab')

    def is_active_sign_in_tab(self):
        self.sign_in_tab.check_attribute('data-state', 'active')

    def is_active_sign_up_tab(self):
        self.sign_up_tab.check_attribute('data-state', 'active')
