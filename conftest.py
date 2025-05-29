import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage
from pages.lifetime_membership_page import LifetimeMembershipPage
from pages.login_page import LoginPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def lifetime_membership_page(driver):
    return LifetimeMembershipPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver)
