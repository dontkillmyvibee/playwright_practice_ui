import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.input import Input
from elements.text import Text


class SignUpFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sign_up_title = Text(page, '//div[text()="Sign Up"]', 'Sign Up title')
        self.sign_up_subtitle = Text(
            page,
            '//div[text()="Create a new account to get started."]',
            'Sign Up subtitle'
        )
        self.name_input = Input(page, '//input[@id="sign-up-name"]', 'Name input')
        self.email_input = Input(page, '//input[@id="sign-up-email"]', 'Email input')
        self.password_input = Input(page, '//input[@id="sign-up-password"]', 'Password input')
        self.confirm_password_input = Input(page, 'sign-up-confirm-password', 'Confirm password input')
        self.name_input_title = Text(page, '//label[@for="«r38»-form-item"]', 'Name input title')
        self.email_input_title = Text(page, '//label[@for="«r39»-form-item"]', 'Email input title')
        self.password_input_title = Text(page, '//label[@for="«r3a»-form-item"]', 'Password input title')
        self.confirm_password_input_title = Text(
            page,
            '//label[@for="«r3b»-form-item"]',
            'Confirm password input title'
        )
        self.password_eye_toggle = Button(
            page,
            '//button[@id="toggle-sign-up-password"]',
            'Password eye toggle'
        )
        self.password_eye_toggle_span = Text(
            page,
            '//button[@id="toggle-sign-up-password"]//span',
            'Password eye toggle span'
        )
        self.confirm_password_eye_toggle = Button(
            page,
            '//button[@id="toggle-sign-up-confirm-password"]',
            'Confirm password eye toggle'
        )
        self.confirm_password_eye_toggle_span = Text(
            page,
            '//button[@id="toggle-sign-up-confirm-password"]//span',
            'Confirm password eye toggle span'
        )
        self.sign_up_button = Button(page, '//button[@id="sign-up-submit"]', 'Sign up button')
        self.sign_in_link = Button(page, '//button[@id="go-to-sign-in"]', 'Sign in link')
        self.password_requirements = Text(
            page,
            '//p[@id="«r3a»-form-item-description"]',
            'Password requirements'
        )
    @allure.step('Checking visible elements')
    def check_visible(self):
        self.sign_up_title.check_visible()
        self.sign_up_subtitle.check_visible()
        self.name_input.check_visible()
        self.email_input.check_visible()
        self.password_input.check_visible()
        self.confirm_password_input.check_visible()
        self.name_input_title.check_visible()
        self.email_input_title.check_visible()
        self.password_input_title.check_visible()
        self.confirm_password_input_title.check_visible()
        self.sign_up_button.check_visible()
        self.sign_in_link.check_visible()
        self.password_requirements.check_visible()

    @allure.step('Checking eye toggle off (password field)')
    def check_password_eye_off(self):
        self.password_eye_toggle_span.check_have_text('Show password')
        self.email_input.check_attribute('type', 'password')

    @allure.step('Checking eye toggle on (password field)')
    def check_password_eye_on(self):
        self.password_eye_toggle_span.check_have_text('Hide password')
        self.email_input.check_attribute('type', 'text')

    @allure.step('Checking eye toggle off(confirm password field)')
    def check_confirm_password_eye_off(self):
        self.confirm_password_eye_toggle_span.check_have_text('Show password')
        self.email_input.check_attribute('type', 'password')

    @allure.step('Checking eye toggle on(confirm password field)')
    def check_confirm_password_eye_on(self):
        self.confirm_password_eye_toggle_span.check_have_text('Hide password')
        self.email_input.check_attribute('type', 'text')

    @allure.step('Filling form with eyes toggles on')
    def fill_form_eyes_toggles_on(self, name: str, email: str, password: str):
        self.check_password_eye_on()
        self.check_confirm_password_eye_on()
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)

    @allure.step('Filling form with eyes toggles off')
    def fill_form_eyes_toggles_off(self, name: str, email: str, password: str):
        self.check_password_eye_off()
        self.check_confirm_password_eye_off()
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)

    @allure.step('On eye toggle(password field)')
    def password_eye_toggle_on(self):
        self.check_password_eye_off()
        self.password_eye_toggle.click()
        self.check_password_eye_on()

    @allure.step('On eye toggle(confirm password field)')
    def confirm_password_eye_toggle_on(self):
        self.check_confirm_password_eye_off()
        self.confirm_password_eye_toggle.click()
        self.check_confirm_password_eye_on()

    @allure.step('Off eye toggle(password field)')
    def password_eye_toggle_off(self):
        self.check_password_eye_on()
        self.password_eye_toggle.click()
        self.check_password_eye_off()

    @allure.step('Off eye toggle(confirm password field)')
    def confirm_password_eye_toggle_off(self):
        self.check_confirm_password_eye_on()
        self.confirm_password_eye_toggle.click()
        self.check_confirm_password_eye_off()

    def sign_up(self): # доработать что попадаю на страничку пользака
        self.sign_up_button.click()