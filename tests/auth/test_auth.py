from pages.authentication_page import AuthenticationPage


class TestSignIn:
    def test_successful_sign_in(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.is_active_sign_in_tab()
        auth_page.sign_in_form.check_visible()
        auth_page.sign_in_form.fill_form_eye_toggle_on(email='username@gmail.com', password='qwerty1234')
        auth_page.sign_in_form.sign_in_button.click()
        auth_page.user_profile_form.check_visible()
        auth_page.user_profile_form.check_titles_and_subtitles_text(email='username@gmail.com')
        auth_page.user_profile_form.check_logout_button_enabled()
        auth_page.user_profile_form.click_logout_button()
        auth_page.is_active_sign_in_tab()
