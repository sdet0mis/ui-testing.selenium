import pytest
from faker import Faker

from pages.login_page import LoginPage


@pytest.mark.smoke
class TestLoginPage:
    def test_fields_are_displayed(self, login_page: LoginPage):
        login_page.open_page()
        login_page.username_field_is_displayed()
        login_page.password_field_is_displayed()
        login_button_is_disabled = (
            login_page.find_login_button().get_attribute("disabled")
        )
        assert login_button_is_disabled == "true", \
            "Кнопка Login не задизейблена"

    def test_login_with_valid_credentials(self, login_page: LoginPage):
        login_page.open_page()
        login_page.enter_username_field("angular")
        login_page.enter_password_field("password")
        login_page.enter_username_description_field("angular")
        login_page.click_login_button()
        message = login_page.find_success_message()
        assert message.text == "You're logged in!!", \
            f"Некорректное сообщение: {message.text}"

    def test_login_with_invalid_credentials(self, login_page: LoginPage):
        login_page.open_page()
        login_page.enter_username_field(Faker().user_name())
        login_page.enter_password_field(Faker().password())
        login_page.enter_username_description_field(Faker().user_name())
        login_page.click_login_button()
        message = login_page.find_error_message()
        assert message.text == "Username or password is incorrect", \
            f"Некорректное сообщение: {message.text}"

    def test_logout(self, login_page: LoginPage):
        login_page.open_page()
        login_page.enter_username_field("angular")
        login_page.enter_password_field("password")
        login_page.enter_username_description_field("angular")
        login_page.click_login_button()
        login_page.click_logout_button()
        login_page.username_field_is_displayed()
        login_page.password_field_is_displayed()
