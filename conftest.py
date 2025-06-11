import os

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
from utils.driver_factory import DriverFactory

load_dotenv()


@pytest.fixture(params=os.getenv("BROWSERS").split(","))
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
def credentials(request: pytest.FixtureRequest) -> tuple:
    if request.param == "wrong_credentials":
        return Faker().user_name(), Faker().password()
    return request.param
