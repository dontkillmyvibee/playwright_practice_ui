import pytest

from config import settings
from pages.authentication_page import AuthenticationPage


@pytest.mark.sign_in_tests
class TestSignIn:
    @pytest.mark.e2e
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

    def test_sign_in_with_invalid_email(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.sign_in_form.fill_form_eye_toggle_on(email='invalidmail', password=settings.test_user.password)
        auth_page.sign_in_form.click_sign_in()
        auth_page.sign_in_form.check_invalid_email_message()

    def test_sign_in_with_invalid_password(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.sign_in_form.fill_form_eye_toggle_on(email=settings.test_user.email, password='qwerty')
        auth_page.sign_in_form.click_sign_in()
        auth_page.sign_in_form.check_invalid_password_message()

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

    def test_sign_in_without_email_and_password(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.sign_in_form.click_sign_in()
        auth_page.sign_in_form.check_invalid_email_message()
        auth_page.sign_in_form.check_invalid_password_message()

