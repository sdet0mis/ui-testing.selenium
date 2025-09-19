from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class LifetimeMembershipPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/lifetime-membership-club/"
