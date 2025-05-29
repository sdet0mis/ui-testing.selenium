import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
        self.action = ActionChains(driver)
        self.URL = None

    def open_page(self) -> None:
        with allure.step(f"Открыть страницу {self.URL}"):
            self.driver.get(self.URL)

    def page_is_opened(self) -> None:
        self.wait.until(EC.url_to_be(self.URL))

    def get_page_title(self) -> str:
        return self.driver.title

    def scroll_to_bottom(self) -> None:
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

    def find_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple) -> list[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def element_is_displayed(self, locator: tuple) -> None:
        assert self.find_element(locator).is_displayed(), \
            f"Элемент {locator} не отображается"

    def fill_field(self, locator: tuple, data: str) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(
            data
        )

    def click(self, locator: tuple) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()
