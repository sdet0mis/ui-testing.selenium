import allure
import pytest

from data import cookies
from pages.sql_page import SQLPage


@allure.epic("UI")
@allure.feature("Страница SQL")
@pytest.mark.smoke
class TestSQLPage:
    @allure.title("Авторизация")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, sql_page: SQLPage):
        try:
            cookie = cookies.get_cookie()
            sql_page.delete_cookie("PHPSESSID")
            sql_page.add_cookie(cookie)
            sql_page.refresh_page()
        except FileNotFoundError:
            sql_page.enter_login(sql_page.LOGIN)
            sql_page.enter_password(sql_page.PASSWORD)
            sql_page.click_enter_button()
            cookies.save_cookie(sql_page.get_cookie("PHPSESSID"))
        nickname = (
            sql_page.find_right_header()
            .text[-(len(sql_page.NICKNAME)):]
        )
        assert nickname == sql_page.NICKNAME, \
            f"Некорректный никнейм: {nickname}"
