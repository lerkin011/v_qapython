from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError
    #
    # def open_login_page(self):
    #     self.driver.get('https://fe-app.stage.nogin.com/log_in')

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def find_elements(self, *args):
        by, val = args[0]
        return self.driver.find_elements(by, val)

