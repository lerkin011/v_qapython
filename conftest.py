from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_email_field.send_keys("ogooglechormea@nieise.com")
    login_page.login_password_field.send_keys("12345678")
    login_page.login_button.click()
    base_page = BasePage(driver)
    base_page.expand_sidebar.click()
    base_page.settings_link.click()
    yield driver
    driver.quit()
