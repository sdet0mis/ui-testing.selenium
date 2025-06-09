import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class AlertPage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.URL = "https://way2automation.com/way2auto_jquery/alert.php"
        self.INPUT_ALERT_IFRAME = (
            By.XPATH, "//iframe[@src='alert/input-alert.html']"
        )
        self.INPUT_ALERT_BUTTON = (By.XPATH, "//a[@href='#example-1-tab-2']")
        self.DISPLAY_ALERT_BUTTON = (
            By.XPATH, "//p[@id='demo']/preceding-sibling::button"
        )
        self.ALERT_TEXT = (By.XPATH, "//p[@id='demo']")

    def switch_to_input_alert_iframe(self) -> None:
        self.driver.switch_to.frame(
            self.find_element(self.INPUT_ALERT_IFRAME)
        )

    @allure.step("Нажать на кнопку Input Alert")
    def click_input_alert_button(self) -> None:
        self.click(self.INPUT_ALERT_BUTTON)

    @allure.step("Нажать на кнопку вывода алерта")
    def click_display_alert_button(self) -> None:
        self.click(self.DISPLAY_ALERT_BUTTON)

    @allure.step("Ввести текст {text} в алерт")
    def enter_text_in_alert(self, text: str) -> None:
        alert = self.get_alert()
        alert.send_keys(text)
        alert.accept()

    def find_alert_text(self) -> WebElement:
        return self.find_element(self.ALERT_TEXT)
