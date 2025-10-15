import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.authentication_page import AuthenticationPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@pytest.mark.sign_up_tests
@allure.epic(AllureEpic.AUTHENTICATION)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.SIGN_UP)
@allure.parent_suite(AllureEpic.AUTHENTICATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.SIGN_UP)
class TestSignUp:
    @pytest.mark.e2e
    @allure.title('Successful sign up')
    @allure.severity(Severity.BLOCKER)
    def test_successful_sign_up(self, auth_page: AuthenticationPage):
        auth_page.visit(auth_page.url)
        auth_page.go_to_sign_up_tab()
        auth_page.is_active_sign_up_tab()
        auth_page.sign_up_form.fill_form_eyes_toggles_on(
            name=settings.test_user.username,
            email=settings.test_user.email,
            password=settings.test_user.password
        )
        auth_page.sign_up_form.click_sign_up()
        auth_page.user_profile_form.check_visible()
        auth_page.user_profile_form.check_titles_and_subtitles_text(
            username=settings.test_user.username,
            email=settings.test_user.email,
            is_signed_up=True
        )
        auth_page.user_profile_form.check_logout_button_enabled()
        auth_page.user_profile_form.click_logout_button()
        auth_page.is_active_sign_in_tab()

