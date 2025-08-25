import random

import allure
import pytest
from faker import Faker
from selenium.common.exceptions import TimeoutException

from pages.banking_app_page import BankingAppPage
from pages.sample_form_page import SampleFormPage
from pages.bank_manager_login_page import BankManagerLoginPage
from pages.add_customer_page import AddCustomerPage
from pages.open_account_page import OpenAccountPage
from pages.customer_login_page import CustomerLoginPage
from pages.customer_account_page import CustomerAccountPage
from pages.customers_page import CustomersPage


@allure.epic("UI")
@allure.feature("Страница банковского приложения")
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
class TestBankingAppPage:
    @allure.title("Успешная регистрация пользователя")
    def test_registration_with_correct_data(
        self,
        banking_app_page: BankingAppPage,
        sample_form_page: SampleFormPage,
    ):
        banking_app_page.click_sample_form_button()
        sample_form_page.page_is_opened()
        sample_form_page.enter_first_name(Faker().first_name())
        sample_form_page.enter_last_name(Faker().last_name())
        sample_form_page.enter_email(Faker().email())
        sample_form_page.enter_password(Faker().password())
        sample_form_page.select_sports_hobby()
        sample_form_page.select_random_gender()
        sample_form_page.enter_about_yourself(
            f"Самое длинное слово из предложенных хобби - \
                {sample_form_page.get_longest_hobby()}"
        )
        sample_form_page.click_register_button()
        sample_form_page.success_message_is_displayed()

    @allure.title("Добавление покупателя")
    def test_add_customer(
        self,
        banking_app_page: BankingAppPage,
        bank_manager_login_page: BankManagerLoginPage,
        add_customer_page: AddCustomerPage,
        customer: any,
    ):
        banking_app_page.click_bank_manager_login_button()
        bank_manager_login_page.click_add_customer_button()
        add_customer_page.enter_first_name(customer.first_name)
        add_customer_page.enter_last_name(customer.last_name)
        add_customer_page.enter_post_code(customer.post_code)
        add_customer_page.click_add_customer_button_2()
        alert = add_customer_page.get_alert()
        assert "Customer added successfully" in alert.text, \
            f"Покупатель не добавлен: {alert.text}"
        alert.accept()

    @allure.title("Открытие аккаунта")
    def test_open_account(
        self,
        open_account_page: OpenAccountPage,
        customer: any,
    ):
        open_account_page.click_open_account_button()
        open_account_page.select_customer(
            f"{customer.first_name} {customer.last_name}"
        )
        open_account_page.select_random_currency()
        open_account_page.click_process_button()
        alert = open_account_page.get_alert()
        assert "Account created successfully" in alert.text, \
            f"Аккаунт не открылся: {alert.text}"
        alert.accept()

    @allure.title("Проверка авторизации покупателя")
    def test_customer_login(
        self,
        banking_app_page: BankingAppPage,
        customer_login_page: CustomerLoginPage,
        customer_account_page: CustomerAccountPage,
        customer: any,
    ):
        banking_app_page.click_customer_login_button()
        customer_login_page.select_customer(
            f"{customer.first_name} {customer.last_name}"
        )
        customer_login_page.click_login_button()
        message = customer_account_page.get_customer_welcome_message()
        assert message == f"{customer.first_name} {customer.last_name}", \
            f"Некорректное сообщение: {message}"

    @allure.title("Успешное пополнение счета")
    def test_deposit(
        self,
        customer_account_page: CustomerAccountPage,
        customer: any,
    ):
        customer_account_page.click_deposit_button()
        customer_account_page.enter_amount("100321")
        customer_account_page.click_deposit_submit_button()
        customer_account_page.check_info_message("Deposit Successful")
        customer_account_page.click_transactions_button()
        customer_account_page.check_last_transaction("Credit", "100321")

    @allure.title("Неуспешное пополнение счета")
    def test_deposit_with_invalid_amount(
        self,
        customer_account_page: CustomerAccountPage,
    ):
        customer_account_page.open_page()
        customer_account_page.click_deposit_button()
        customer_account_page.enter_amount("0")
        customer_account_page.click_deposit_submit_button()
        customer_account_page.check_info_message("none")
        customer_account_page.click_transactions_button()
        customer_account_page.check_last_transaction("none", "0")

    @allure.title("Успешное снятие средств")
    def test_withdraw(
        self,
        customer_account_page: CustomerAccountPage,
    ):
        customer_account_page.open_page()
        balance = customer_account_page.get_customer_balance()
        customer_account_page.click_withdraw_button()
        customer_account_page.enter_amount(
            amount := random.randint(1, int(balance))
        )
        customer_account_page.click_withdraw_submit_button()
        customer_account_page.check_info_message("Transaction successful")
        customer_account_page.click_transactions_button()
        customer_account_page.check_last_transaction(
            "Debit", str(amount)
        )

    @allure.title("Неуспешное снятие средств")
    def test_withdraw_with_invalid_amount(
        self,
        customer_account_page: CustomerAccountPage,
    ):
        customer_account_page.open_page()
        customer_account_page.click_withdraw_button()
        customer_account_page.enter_amount("1000000")
        customer_account_page.click_withdraw_submit_button()
        customer_account_page.check_info_message(
            "Transaction Failed. You can not withdraw amount more than the balance."  # noqa
        )
        customer_account_page.click_transactions_button()
        customer_account_page.check_last_transaction("none", "1000000")

    @allure.title("Проверка баланса")
    def test_check_balance(
        self,
        customer_account_page: CustomerAccountPage,
    ):
        customer_account_page.open_page()
        balance = customer_account_page.get_customer_balance()
        customer_account_page.click_transactions_button()
        customer_account_page.check_balance(balance)

    @allure.title("Снятие оставшихся средств")
    def test_withdraw_all_balance(
        self,
        customer_account_page: CustomerAccountPage,
    ):
        customer_account_page.open_page()
        balance = customer_account_page.get_customer_balance()
        customer_account_page.click_withdraw_button()
        customer_account_page.enter_amount(balance)
        customer_account_page.click_withdraw_submit_button()
        customer_account_page.check_info_message("Transaction successful")
        balance = customer_account_page.get_customer_balance()
        assert balance == "0", f"Баланс не равен 0: {balance}"

    @allure.title("Очистка истории транзакций")
    def test_clear_transactions_history(
        self,
        customer_account_page: CustomerAccountPage,
    ):
        customer_account_page.open_page()
        customer_account_page.click_transactions_button()
        assert len(
            customer_account_page.get_table_transactions()
        ) > 0
        customer_account_page.click_reset_button()
        try:
            assert len(
                customer_account_page.get_table_transactions()
            ) == 0
        except TimeoutException:
            assert True
        customer_account_page.click_back_button()
        balance = customer_account_page.get_customer_balance()
        assert balance == "0", \
            f"Баланс не равен 0: {balance}"

    @allure.title("Удаление покупателя")
    def test_delete_customer(
        self,
        bank_manager_login_page: BankManagerLoginPage,
        customers_page: CustomersPage,
        customer: any,
    ):
        bank_manager_login_page.open_page()
        bank_manager_login_page.click_customers_button()
        customers_page.enter_customer_name(customer.first_name)
        customers_page.delete_customer_button_is_displayed()
        customers_page.click_delete_customer_button()
        customers_page.clear_search_customer_field()
        assert (
            customer.first_name not in customers_page.get_customers_names()
        ), f"Покупатель не удален: {customer.first_name}"
