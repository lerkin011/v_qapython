from pages.base_page import BasePage
from selenium.webdriver.common.by import By


login_email_field = (By.ID, "login")
login_password_field = (By.ID, "password")
login_button = (By.XPATH, "//*[@id='root']/div[1]/div/div/div/form/div[3]/button")


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login_page(self):
        self.driver.get('https://fe-app.stage.nogin.com/log_in')

    @property
    def login_email_field(self):
        return self.find_element(login_email_field)

    @property
    def login_password_field(self):
        return self.find_element(login_password_field)

    @property
    def login_button(self):
        return self.find_element(login_button)
