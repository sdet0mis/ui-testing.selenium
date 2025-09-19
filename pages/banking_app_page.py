import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BankingAppPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login" # noqa
        self.SAMPLE_FORM_BUTTON = (By.XPATH, "(//div/a)[1]")
        self.CUSTOMER_LOGIN_BUTTON = (
            By.XPATH, "//button[@ng-click='customer()']"
        )
        self.BANK_MANAGER_LOGIN_BUTTON = (
            By.XPATH, "//button[@ng-click='manager()']"
        )

    @allure.step("Нажать кнопку Sample Form")
    def click_sample_form_button(self) -> None:
        self.click(self.SAMPLE_FORM_BUTTON)

    @allure.step("Нажать кнопку Customer Login")
    def click_customer_login_button(self) -> None:
        self.click(self.CUSTOMER_LOGIN_BUTTON)

    @allure.step("Нажать кнопку Bank Manager Login")
    def click_bank_manager_login_button(self) -> None:
        self.click(self.BANK_MANAGER_LOGIN_BUTTON)
