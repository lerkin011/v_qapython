from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

expand_sidebar_button = (By.CLASS_NAME, "show")
settings_link = (By.PARTIAL_LINK_TEXT, "Settings")


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def find_elements(self, *args):
        by, val = args[0]
        return self.driver.find_elements(by, val)

    # def find_element(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
    #                                                   message=f"Can't find element by locator {locator}")
    #
    # def find_elements(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
    #                                                   message=f"Can't find elements by locator {locator}")

    @property
    def expand_sidebar(self):
        return self.find_element(expand_sidebar_button)

    @property
    def settings_link(self):
        return self.find_element(settings_link)

