import os
from dataclasses import make_dataclass, field

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from faker import Faker
from selenium import webdriver

from pages.main_page import MainPage
from pages.lifetime_membership_page import LifetimeMembershipPage
from pages.login_page import LoginPage
from pages.sql_page import SQLPage
from pages.droppable_page import DroppablePage
from pages.frames_and_windows_page import FramesAndWindowsPage
from pages.alert_page import AlertPage
from pages.authentication_page import AuthenticationPage
from pages.banking_app_page import BankingAppPage
from pages.sample_form_page import SampleFormPage
from pages.bank_manager_login_page import BankManagerLoginPage
from pages.add_customer_page import AddCustomerPage
from pages.open_account_page import OpenAccountPage
from pages.customer_login_page import CustomerLoginPage
from pages.customer_account_page import CustomerAccountPage
from pages.customers_page import CustomersPage
from utils.driver_factory import DriverFactory

load_dotenv()


@pytest.fixture(params=os.getenv("BROWSERS").split(","), scope="session")
def driver(request: pytest.FixtureRequest) -> webdriver:
    driver = DriverFactory.get_driver(
        grid=True if os.getenv("GRID") else False,
        browser=request.param
    )
    request.node.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(
    item: pytest.Item, call: pytest.CallInfo
) -> None:
    if call.when == "call" and call.excinfo is not None:
        driver = item.driver
        allure.attach(
            driver.get_screenshot_as_png(),
            "screenshot",
            AttachmentType.PNG
        )


@pytest.fixture
def main_page(driver: webdriver) -> MainPage:
    main_page = MainPage(driver)
    main_page.open_page()
    return main_page


@pytest.fixture
def lifetime_membership_page(driver: webdriver) -> LifetimeMembershipPage:
    return LifetimeMembershipPage(driver)


@pytest.fixture
def login_page(driver: webdriver) -> LoginPage:
    login_page = LoginPage(driver)
    login_page.open_page()
    return login_page


@pytest.fixture
def sql_page(driver: webdriver) -> SQLPage:
    sql_page = SQLPage(driver)
    sql_page.open_page()
    return sql_page


@pytest.fixture
def droppable_page(driver: webdriver) -> DroppablePage:
    droppable_page = DroppablePage(driver)
    droppable_page.open_page()
    return droppable_page


@pytest.fixture
def frames_and_windows_page(driver: webdriver) -> FramesAndWindowsPage:
    frames_and_windows_page = FramesAndWindowsPage(driver)
    frames_and_windows_page.open_page()
    return frames_and_windows_page


@pytest.fixture
def alert_page(driver: webdriver) -> AlertPage:
    alert_page = AlertPage(driver)
    alert_page.open_page()
    return alert_page


@pytest.fixture
def authentication_page(driver: webdriver) -> AuthenticationPage:
    authentication_page = AuthenticationPage(driver)
    authentication_page.open_page()
    return authentication_page


@pytest.fixture
def banking_app_page(driver: webdriver) -> BankingAppPage:
    banking_app_page = BankingAppPage(driver)
    banking_app_page.open_page()
    return banking_app_page


@pytest.fixture
def sample_form_page(driver: webdriver) -> SampleFormPage:
    sample_form_page = SampleFormPage(driver)
    return sample_form_page


@pytest.fixture
def bank_manager_login_page(driver: webdriver) -> BankManagerLoginPage:
    bank_manager_login_page = BankManagerLoginPage(driver)
    return bank_manager_login_page


@pytest.fixture
def add_customer_page(driver: webdriver) -> AddCustomerPage:
    add_customer_page = AddCustomerPage(driver)
    return add_customer_page


@pytest.fixture
def open_account_page(driver: webdriver) -> OpenAccountPage:
    open_account_page = OpenAccountPage(driver)
    return open_account_page


@pytest.fixture
def customer_login_page(driver: webdriver) -> CustomerLoginPage:
    customer_login_page = CustomerLoginPage(driver)
    return customer_login_page


@pytest.fixture
def customer_account_page(driver: webdriver) -> CustomerAccountPage:
    customer_account_page = CustomerAccountPage(driver)
    return customer_account_page


@pytest.fixture
def customers_page(driver: webdriver) -> CustomersPage:
    customers_page = CustomersPage(driver)
    return customers_page


@pytest.fixture(scope="session")
def customer() -> any:
    if not hasattr(customer, "created_customer"):
        Customer = make_dataclass(
            "Customer",
            [
                ("first_name", str, field(default_factory=lambda: Faker().first_name())), # noqa
                ("last_name", str, field(default_factory=lambda: Faker().last_name())), # noqa
                ("post_code", str, field(default_factory=lambda: Faker().postcode())),  # noqa
            ]
        )
        customer.created_customer = Customer()
    return customer.created_customer


@pytest.fixture
def credentials(request: pytest.FixtureRequest) -> tuple:
    if request.param == "wrong_credentials":
        return Faker().user_name(), Faker().password()
    return request.param
