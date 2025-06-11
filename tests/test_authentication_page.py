import allure
import pytest

from pages.authentication_page import AuthenticationPage


@allure.epic("UI")
@allure.feature("Страница авторизации")
@pytest.mark.smoke
class TestAuthenticationPage:
    @allure.title("Авторизация")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_authentication(self, authentication_page: AuthenticationPage):
        authentication_page.click_display_image_button()
        authentication_page.open_image_page()
        authentication_page.authenticated_image_is_displayed()
        image_attribute = (
            authentication_page.find_authenticated_image().get_attribute("src")
        )
        assert authentication_page.CREDENTIALS in image_attribute, \
            f"Некорректная картинка: {image_attribute}"
