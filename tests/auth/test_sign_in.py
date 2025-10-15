import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication_page import AuthenticationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.sign_in_tests
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.SIGN_IN)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.SIGN_IN)
class TestSignIn:
    @pytest.mark.e2e
    @allure.title('Successful sign in')
    @allure.severity(Severity.BLOCKER)
    def test_successful_sign_in(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.is_active_sign_in_tab()
        auth_page.sign_in_form.check_visible()
        auth_page.sign_in_form.fill_form_eye_toggle_on(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        auth_page.sign_in_form.click_sign_in()
        auth_page.user_profile_form.check_visible()
        auth_page.user_profile_form.check_titles_and_subtitles_text(email=settings.test_user.email)
        auth_page.user_profile_form.check_logout_button_enabled()
        auth_page.user_profile_form.click_logout_button()
        auth_page.is_active_sign_in_tab()

    @allure.title('Sign in with invalid email')
    def test_sign_in_with_invalid_email(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.sign_in_form.fill_form_eye_toggle_on(
            email=settings.test_invalid_user.email,
            password=settings.test_user.password
        )
        auth_page.sign_in_form.click_sign_in()
        auth_page.sign_in_form.check_invalid_email_message()

    @allure.title('Sign in with invalid password')
    def test_sign_in_with_invalid_password(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.sign_in_form.fill_form_eye_toggle_on(
            email=settings.test_user.email,
            password=settings.test_invalid_user.password
        )
        auth_page.sign_in_form.click_sign_in()
        auth_page.sign_in_form.check_invalid_password_message()

    @allure.title('Successful sign in with eye toggle off')
    @pytest.mark.e2e
    def test_successful_sign_in_with_eye_off(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.is_active_sign_in_tab()
        auth_page.sign_in_form.check_visible()
        auth_page.sign_in_form.fill_form_eye_toggle_off(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        auth_page.sign_in_form.click_sign_in()
        auth_page.user_profile_form.check_visible()
        auth_page.user_profile_form.check_titles_and_subtitles_text(email=settings.test_user.email)
        auth_page.user_profile_form.check_logout_button_enabled()
        auth_page.user_profile_form.click_logout_button()
        auth_page.is_active_sign_in_tab()

    @allure.title('Successful sign in form fill')
    def test_successful_sign_in_form_fill(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.is_active_sign_in_tab()
        auth_page.sign_in_form.fill_form_eye_toggle_on(
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        auth_page.sign_in_form.check_fill(
            email=settings.test_user.email,
            password=settings.test_user.password
        )

    @allure.title('Sign in without email and password')
    def test_sign_in_without_email_and_password(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.sign_in_form.click_sign_in()
        auth_page.sign_in_form.check_invalid_email_message()
        auth_page.sign_in_form.check_invalid_password_message()

