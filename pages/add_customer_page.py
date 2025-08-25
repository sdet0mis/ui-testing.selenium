import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.bank_manager_login_page import BankManagerLoginPage


class AddCustomerPage(BankManagerLoginPage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/#/manager/addCust" # noqa
        self.FIRST_NAME_FIELD = (By.XPATH, "//input[@ng-model='fName']")
        self.LAST_NAME_FIELD = (By.XPATH, "//input[@ng-model='lName']")
        self.POST_CODE_FIELD = (By.XPATH, "//input[@ng-model='postCd']")
        self.ADD_CUSTOMER_BUTTON_2 = (By.XPATH, "//button[@type='submit']")

    @allure.step("Ввести {first_name} в поле First Name")
    def enter_first_name(self, first_name: str) -> None:
        self.fill_field(self.FIRST_NAME_FIELD, first_name)

    @allure.step("Ввести {last_name} в поле Last Name")
    def enter_last_name(self, last_name: str) -> None:
        self.fill_field(self.LAST_NAME_FIELD, last_name)

    @allure.step("Ввести {post_code} в поле Post Code")
    def enter_post_code(self, post_code: str) -> None:
        self.fill_field(self.POST_CODE_FIELD, post_code)

    @allure.step("Нажать кнопку Add Customer под полем Post Code")
    def click_add_customer_button_2(self) -> None:
        self.click(self.ADD_CUSTOMER_BUTTON_2)
