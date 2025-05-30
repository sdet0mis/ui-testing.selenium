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
    @pytest.mark.parametrize("run", range(2))
    def test_login(self, run: int, sql_page: SQLPage):
        try:
            cookie = cookies.get_cookie_from_file()
            sql_page.delete_cookie("PHPSESSID")
            sql_page.add_cookie(cookie)
            sql_page.refresh_page()
            cookies.delete_cookie_file()
        except FileNotFoundError:
            sql_page.enter_login(sql_page.LOGIN)
            sql_page.enter_password(sql_page.PASSWORD)
            sql_page.click_enter_button()
            cookies.save_cookie(sql_page.get_cookie("PHPSESSID"))
        right_header_text = sql_page.find_right_header().text
        nickname_length = len(sql_page.NICKNAME)
        nickname = right_header_text[-nickname_length:]
        assert nickname == sql_page.NICKNAME, \
            f"Некорректный никнейм: {nickname}"
