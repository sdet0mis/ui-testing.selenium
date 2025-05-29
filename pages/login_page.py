from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"  # noqa
        self.USERNAME_FIELD = (By.ID, "username")
        self.PASSWORD_FIELD = (By.ID, "password")
        self.USERNAME_DESCRIPTION_FIELD = (
            By.XPATH, "//input[@id='formly_1_input_username_0']"
        )
        self.LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-danger']")
        self.ERROR_MESSAGE = (
            By.XPATH, "//div[@class='alert alert-danger ng-binding ng-scope']"
        )
        self.SUCCESS_MESSAGE = (
            By.XPATH, "(//p[@class='ng-scope'])[1]"
        )
        self.LOGOUT_BUTTON = (By.XPATH, "//p[@class='ng-scope']/a")

    def username_field_is_displayed(self):
        self.element_is_displayed(self.USERNAME_FIELD)

    def enter_username_field(self, username):
        self.fill_field(self.USERNAME_FIELD, username)

    def password_field_is_displayed(self):
        self.element_is_displayed(self.PASSWORD_FIELD)

    def enter_password_field(self, password):
        self.fill_field(self.PASSWORD_FIELD, password)

    def enter_username_description_field(self, username_description):
        self.fill_field(
            self.USERNAME_DESCRIPTION_FIELD, username_description
        )

    def find_login_button(self):
        return self.find_element(self.LOGIN_BUTTON)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def find_error_message(self):
        return self.find_element(self.ERROR_MESSAGE)

    def find_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE)

    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)
