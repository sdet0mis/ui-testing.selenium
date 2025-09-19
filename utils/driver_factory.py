import platform

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.common.options import ArgOptions


class DriverFactory:
    @staticmethod
    def get_driver(grid: bool, browser: str) -> WebDriver:
        options = DriverFactory._options(browser)
        if browser == "ie":
            if not grid and platform.system() != "Windows":
                raise Exception("Браузер IE поддерживается только на Windows")
            DriverFactory._ie_settings(options)
        else:
            DriverFactory._arguments(options)
        if grid:
            return webdriver.Remote(
                command_executor="http://localhost:4444",
                options=options
            )
        return DriverFactory._driver(browser, options)

    @staticmethod
    def _options(browser: str) -> ArgOptions:
        if browser == "chrome":
            return ChromeOptions()
        elif browser == "firefox":
            return FirefoxOptions()
        elif browser == "edge":
            return EdgeOptions()
        elif browser == "ie":
            return IEOptions()
        else:
            raise Exception("Неккоректное название браузера")

    @staticmethod
    def _arguments(options: ArgOptions) -> None:
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")

    @staticmethod
    def _ie_settings(options: ArgOptions) -> None:
        options.ignore_protected_mode_settings = True
        options.require_window_focus = True

    @staticmethod
    def _driver(browser: str, options: ArgOptions) -> WebDriver:
        if browser == "chrome":
            return webdriver.Chrome(options)
        elif browser == "firefox":
            return webdriver.Firefox(options)
        elif browser == "edge":
            return webdriver.Edge(options)
        elif browser == "ie":
            return webdriver.Ie(options, executable_path="IEDriverServer.exe")
