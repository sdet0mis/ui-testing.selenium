import random

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SampleFormPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/registrationform.html" # noqa
        self.FIRST_NAME_FIELD = (By.ID, "firstName")
        self.LAST_NAME_FIELD = (By.ID, "lastName")
        self.EMAIL_FIELD = (By.ID, "email")
        self.PASSWORD_FIELD = (By.ID, "password")
        self.SPORTS_CHECKBOX = (By.XPATH, "//input[@value='Sports']")
        self.HOBBIES_CHECKBOXES = (By.XPATH, "//label/input")
        self.GENDER_DROPDOWN_LIST = (By.ID, "gender")
        self.ABOUT_YOURSELF_TEXTAREA = (By.ID, "about")
        self.REGISTER_BUTTON = (By.XPATH, "//div/button")
        self.SUCCESS_MESSAGE = (By.ID, "successMessage")

    @allure.step("Ввести {first_name} в поле First Name")
    def enter_first_name(self, first_name: str) -> None:
        self.fill_field(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Ввести {last_name} в поле Last Name")
    def enter_last_name(self, last_name: str) -> None:
        self.fill_field(self.LAST_NAME_FIELD, last_name)

    @allure.step("Ввести {email} в поле Email")
    def enter_email(self, email: str) -> None:
        self.fill_field(self.EMAIL_FIELD, email)

    @allure.step("Ввести {password} в поле Password")
    def enter_password(self, password: str) -> None:
        self.fill_field(self.PASSWORD_FIELD, password)

    @allure.step("Выбрать чекбокс Sports в блоке Hobbies")
    def select_sports_hobby(self) -> None:
        self.click(self.SPORTS_CHECKBOX)

    def get_longest_hobby(self) -> str:
        hobbies_webelements = self.find_elements(self.HOBBIES_CHECKBOXES)
        hobbies_list = [
            hobby.get_attribute("value") for hobby in hobbies_webelements
        ]
        return max(hobbies_list, key=len)

    @allure.step("Выбрать случайный пол в выпадающем списке Gender")
    def select_random_gender(self) -> None:
        gender = random.choice(["male", "female", "other"])
        self.select(self.GENDER_DROPDOWN_LIST).select_by_value(gender)

    @allure.step("Ввести {text} в поле About Yourself")
    def enter_about_yourself(self, text: str) -> None:
        self.fill_field(self.ABOUT_YOURSELF_TEXTAREA, text)

    @allure.step("Нажать на кнопку Register")
    def click_register_button(self) -> None:
        self.click(self.REGISTER_BUTTON)

    def success_message_is_displayed(self) -> None:
        self.element_is_displayed(self.SUCCESS_MESSAGE)
