import allure
import pytest

from pages.frames_and_windows_page import FramesAndWindowsPage


@allure.epic("UI")
@allure.feature("Страница вкладок и окон")
@pytest.mark.smoke
class TestFramesAndWindowsPage:
    @allure.title("Открытие новой вкладки")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_new_browser_tab(
        self, frames_and_windows_page: FramesAndWindowsPage
    ):
        window1 = frames_and_windows_page.get_current_window()
        frames_and_windows_page.switch_to_frame()
        frames_and_windows_page.click_new_browser_tab_link()
        window2 = frames_and_windows_page.get_all_windows()[1]
        frames_and_windows_page.switch_to_window(window2)
        frames_and_windows_page.click_new_browser_tab_link()
        window3 = frames_and_windows_page.get_all_windows()[2]
        assert window3 != window2 and window3 != window1, \
            "Новая вкладка не открылась"
