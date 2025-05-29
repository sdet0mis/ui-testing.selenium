from pages.base_page import BasePage


class LifetimeMembershipPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/lifetime-membership-club/"
