from pages.base_page import BasePage
from selenium.webdriver.common.by import By


login_email_field = (By.ID, "login")
login_password_field = (By.ID, "password")
login_button = (By.CLASS_NAME, "//button[@type='submit']")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_email_field = self.find_element(login_email_field)
        self.login_password_field = self.find_element(login_password_field)
        self.login_button = self.find_element(login_button)

    def open_login_page(self):
        self.driver.get('https://fe-app.stage.nogin.com/log_in')

    # @property
    # def email_field(self):
    #     return self.find_element(login_email_field)
