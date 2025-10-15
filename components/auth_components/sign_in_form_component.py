import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class SignInFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sign_in_title = Text(page, '//div[text()="Sign In"]', 'Sign in title')
        self.sign_in_subtitle = Text(
            page,
            '//div[text()="Enter your credentials to sign in to your account."]',
            'Sign in subtitle'
        )

        self.email_input = Input(page, '//input[@id="sign-in-email"]', 'Email input')
        self.password_input = Input(page, '//input[@id="sign-in-password"]', 'Password')
        self.eye_toggle = Button(page, '//button[@id="toggle-sign-in-password"]', 'Eye toggle')
        self.sign_in_button = Button(page, '//button[@id="sign-in-submit"]', 'Sign in button')
        self.sign_up_link = Button(page, '//button[@id="go-to-sign-up"]', 'Sign up link')
        self.eye_span = Text(page, '//button[@id="toggle-sign-in-password"]/span', 'Eye span')
        self.invalid_email_message = Text(
            page,
            '//p[text()="Please enter a valid email address."]', 'Invalid email message')
        self.invalid_password_message = Text(
            page,
            '//p[text()="Password must be at least 8 characters."]',
            'Invalid password message'
        )

    @allure.step('Checking eye toggle off')
    def check_eye_off(self):
        self.eye_span.check_have_text('Hide password')
        self.password_input.check_attribute('type', 'text')

    @allure.step('Checking eye toggle on')
    def check_eye_on(self):
        self.eye_span.check_have_text('Show password')
        self.password_input.check_attribute('type', 'password')

    @allure.step('Checking visible elements')
    def check_visible(self):
        self.sign_in_title.check_visible()
        self.sign_in_subtitle.check_visible()
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.eye_toggle.check_visible()
        self.sign_in_button.check_visible()
        self.sign_up_link.check_visible()

    @allure.step('Checking text titles and subtitles')
    def check_text_titles_and_subtitles(self):
        self.sign_in_title.check_have_text("Sign In")
        self.sign_in_subtitle.check_have_text("Enter your credentials to sign in to your account.")

    @allure.step('Filling form with eye toggle on')
    def fill_form_eye_toggle_on(self, email: str, password: str):
        self.check_eye_on()
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step('Filling form with eye toggle off')
    def fill_form_eye_toggle_off(self, email: str, password: str):
        self.check_eye_on()
        self.off_eye_toggle()
        self.check_eye_off()
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_sign_in(self):
        self.sign_in_button.click()

    @allure.step('On eye toggle')
    def on_eye_toggle(self):
        self.check_eye_off()
        self.eye_toggle.click()
        self.check_eye_on()

    @allure.step('Off eye toggle')
    def off_eye_toggle(self):
        self.check_eye_on()
        self.eye_toggle.click()
        self.check_eye_off()

    def click_sign_up_link(self):
        self.sign_up_link.click()

    @allure.step('Checking invalid email message')
    def check_invalid_email_message(self):
        self.invalid_email_message.check_visible()
        self.invalid_email_message.check_have_text('Please enter a valid email address.')

    @allure.step('Checking invalid password message')
    def check_invalid_password_message(self):
        self.invalid_password_message.check_visible()
        self.invalid_password_message.check_have_text('Password must be at least 8 characters.')

    @allure.step('Checking fields have values')
    def check_fill(self, email: str, password: str):
        self.email_input.check_have_value(email)
        self.password_input.check_have_value(password)
