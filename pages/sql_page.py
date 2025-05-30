import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SQLPage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.sql-ex.ru/"
        self.LOGIN = "losoxo@azuretechtalk."
        self.LOGIN_FIELD = (By.XPATH, "(//input[@type='text'])[1]")
        self.PASSWORD = "losoxo@azuretechtalk.net"
        self.PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
        self.NICKNAME = "losoxo@azuretechtalk"
        self.ENTER_BUTTON = (By.XPATH, "(//input[@type='submit'])[1]")
        self.RIGHT_HEADER = (By.XPATH, "(//td[@align='right'])[1]")

    @allure.step("Ввести в поле Login {login}")
    def enter_login(self, login: str) -> None:
        self.fill_field(self.LOGIN_FIELD, login)

    @allure.step("Ввести в поле Password {password}")
    def enter_password(self, password: str) -> None:
        self.fill_field(self.PASSWORD_FIELD, password)

    @allure.step("Нажать на кнопку Enter")
    def click_enter_button(self) -> None:
        self.click(self.ENTER_BUTTON)

    def find_right_header(self) -> str:
        return self.find_element(self.RIGHT_HEADER)
