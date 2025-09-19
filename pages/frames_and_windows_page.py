import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FramesAndWindowsPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://way2automation.com/way2auto_jquery/frames-and-windows.php"  # noqa
        self.IFRAME = (By.XPATH, "//iframe[@class='demo-frame']")
        self.NEW_BROWSER_TAB_LINK = (By.XPATH, "//a[@target='_blank']")

    def switch_to_frame(self) -> None:
        self.driver.switch_to.frame(
            self.find_element(self.IFRAME)
        )

    def new_browser_tab_link_is_displayed(self) -> None:
        self.element_is_displayed(self.NEW_BROWSER_TAB_LINK)

    @allure.step("Нажать на ссылку New Browser Tab")
    def click_new_browser_tab_link(self) -> None:
        self.click(self.NEW_BROWSER_TAB_LINK)
