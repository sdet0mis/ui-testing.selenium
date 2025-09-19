import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BankManagerLoginPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager" # noqa
        self.ADD_CUSTOMER_BUTTON = (
            By.XPATH, "//button[@ng-click='addCust()']"
        )
        self.OPEN_ACCOUNT_BUTTON = (
            By.XPATH, "//button[@ng-click='openAccount()']"
        )
        self.CUSTOMERS_BUTTON = (
            By.XPATH, "//button[@ng-click='showCust()']"
        )

    @allure.step("Нажать кнопку Add Customer")
    def click_add_customer_button(self) -> None:
        self.click(self.ADD_CUSTOMER_BUTTON)

    @allure.step("Нажать кнопку Open Account")
    def click_open_account_button(self) -> None:
        self.click(self.OPEN_ACCOUNT_BUTTON)

    @allure.step("Нажать кнопку Customers")
    def click_customers_button(self) -> None:
        self.click(self.CUSTOMERS_BUTTON)
