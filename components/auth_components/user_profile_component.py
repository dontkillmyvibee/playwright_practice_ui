import allure
from playwright.sync_api import Page

from components.auth_components.sign_up_form_component import SignUpFormComponent
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class UserProfileComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.user_profile_title = Text(
            page,
            '//div[@id="user-profile"]//div//div[text()="User Profile"]',
            'User profile title'
        )
        self.user_profile_subtitle = Text(
            page,
            '//div[@id="user-profile"]//div[text()="You are currently logged in."]',
            'User profile subtitle'
        )
        self.successful_auth_message = Text(
            page,
            '//div[@id="user-profile"]//div//div//span[text()="Authentication successful"]',
            'Successful authentication message'
        )
        self.username_title = Text(page,'//span[@id="profile-name"]','Username title')
        self.email_title = Text(page,'//span[@id="profile-email"]','Email title')
        self.logout_button = Button(page, '//button[@id="logout-button"]', 'logout button')

    @allure.step('Checking visible elements')
    def check_visible(self):
        self.user_profile_title.check_visible()
        self.user_profile_subtitle.check_visible()
        self.successful_auth_message.check_visible()
        self.username_title.check_visible()
        self.email_title.check_visible()
        self.logout_button.check_visible()

    @allure.step('Checking titles and subtitles text')
    def check_titles_and_subtitles_text(
            self,
            username: str | None = None,
            email: str | None = None,
            is_signed_up: bool = False
    ):
        self.user_profile_title.check_have_text("User Profile")
        self.user_profile_subtitle.check_have_text("You are currently logged in.")
        self.successful_auth_message.check_have_text("Authentication successful")
        if is_signed_up:
            self.username_title.check_have_text(username)
            self.email_title.check_have_text(email)
        else:
            self.username_title.check_have_text("Test User")
            self.email_title.check_have_text(email)

    def check_logout_button_enabled(self):
        self.logout_button.check_enabled()

    def click_logout_button(self):
        self.logout_button.click()