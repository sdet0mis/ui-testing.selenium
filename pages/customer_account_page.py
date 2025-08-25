import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class CustomerAccountPage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.URL = "https://www.way2automation.com/angularjs-protractor/banking/#/account" # noqa
        self.CUSTOMER_WELCOME_MESSAGE = (By.XPATH, "//strong/span")
        self.CUSTOMER_BALANCE = (
            By.XPATH, "//div/strong[@class='ng-binding'][2]"
        )
        self.TRANSACTIONS_BUTTON = (
            By.XPATH, "//button[@ng-click='transactions()']"
        )
        self.DEPOSIT_BUTTON = (By.XPATH, "//button[@ng-click='deposit()']")
        self.WITHDRAW_BUTTON = (By.XPATH, "//button[@ng-click='withdrawl()']")
        self.AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
        self.INFO_MESSAGE = (By.XPATH, "//span[@ng-show='message']")
        self.DEPOSIT_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
        self.WITHDRAW_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
        self.DATE_TIME_SORT_BUTTON = (By.XPATH, "//a[@href='#']")
        self.TABLE_TRANSACTIONS = (By.XPATH, "//tbody/tr")
        self.LAST_TRANSACTION_AMOUNT = (By.XPATH, "//tr[@id='anchor0']/td[2]")
        self.LAST_TRANSACTION_TYPE = (By.XPATH, "//tr[@id='anchor0']/td[3]")
        self.RESET_BUTTON = (By.XPATH, "//button[@ng-click='reset()']")
        self.BACK_BUTTON = (By.XPATH, "//button[@ng-click='back()']")

    def get_customer_welcome_message(self) -> str:
        return self.find_element(self.CUSTOMER_WELCOME_MESSAGE).text

    def get_customer_balance(self) -> str:
        return self.find_element(self.CUSTOMER_BALANCE).text

    def get_table_transactions(self) -> list[WebElement]:
        return self.find_elements(self.TABLE_TRANSACTIONS)

    @allure.step("Нажать кнопку Transactions")
    def click_transactions_button(self) -> None:
        time.sleep(1)  # Транзакция не появляется в таблице
        self.click(self.TRANSACTIONS_BUTTON)

    @allure.step("Нажать кнопку Deposit")
    def click_deposit_button(self) -> None:
        self.click(self.DEPOSIT_BUTTON)

    @allure.step("Нажать кнопку Withdraw")
    def click_withdraw_button(self) -> None:
        self.click(self.WITHDRAW_BUTTON)

    @allure.step("Ввести сумму {amount} в поле Amount")
    def enter_amount(self, amount: str) -> None:
        self.fill_field(self.AMOUNT_FIELD, amount)

    @allure.step("Нажать кнопку подтверждения Deposit под полем Amount")
    def click_deposit_submit_button(self) -> None:
        self.click(self.DEPOSIT_SUBMIT_BUTTON)

    @allure.step("Нажать кнопку подтверждения Withdraw под полем Amount")
    def click_withdraw_submit_button(self) -> None:
        self.click(self.WITHDRAW_SUBMIT_BUTTON)

    @allure.step("Нажать кнопку Reset")
    def click_reset_button(self) -> None:
        self.click(self.RESET_BUTTON)

    @allure.step("Нажать кнопку Back")
    def click_back_button(self) -> None:
        self.click(self.BACK_BUTTON)

    def check_info_message(self, text: str) -> None:
        message = self.find_element(self.INFO_MESSAGE)
        if text == "none":
            assert not message.is_displayed(), \
                "Сообщение отображается"
        else:
            assert message.is_displayed(), \
                "Сообщение не отображается"
            assert message.text == text, \
                f"Некорректное сообщение: {message.text}"

    def check_last_transaction(self, t_type: str, amount: str) -> None:
        self.click(self.DATE_TIME_SORT_BUTTON)
        last_transaction_amount = self.find_element(
            self.LAST_TRANSACTION_AMOUNT
        ).text
        if t_type == "none":
            assert last_transaction_amount != amount, \
                f"Транзакция прошла, сумма: {last_transaction_amount}"
        else:
            last_transaction_type = self.find_element(
                self.LAST_TRANSACTION_TYPE
            ).text
            assert last_transaction_type == t_type and \
                last_transaction_amount == amount, \
                f"Некорректная транзакция: \
                    {last_transaction_type} {last_transaction_amount}"

    def check_balance(self, balance: str) -> None:
        table_balance = 0
        transactions = [
            transaction.text for transaction in self.get_table_transactions()
            ]
        for transaction in transactions:
            t_type, amount = transaction.split()[-1], int(
                transaction.split()[-2]
            )
            if t_type == "Credit":
                table_balance += amount
            elif t_type == "Debit":
                table_balance -= amount
        assert str(table_balance) == balance, \
            f"Некорректный баланс: {str(table_balance)} != {balance}"
