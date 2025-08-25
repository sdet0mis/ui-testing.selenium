import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CustomerLoginPage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/#/customer" # noqa
        self.YOUR_NAME_DROPDOWN_LIST = (By.ID, "userSelect")
        self.LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    @allure.step("Выбрать пользователя")
    def select_customer(self, customer: str) -> None:
        self.select(
            self.YOUR_NAME_DROPDOWN_LIST
        ).select_by_visible_text(customer)

    @allure.step("Нажать кнопку Login")
    def click_login_button(self) -> None:
        self.click(self.LOGIN_BUTTON)
