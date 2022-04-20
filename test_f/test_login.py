from pages.login_page import LoginPage
from time import sleep


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login_email_field.send_keys("ogooglechormea@nieise.com")
    login_page.login_password_field.send_keys("12345678")
    login_page.login_button.click()
    sleep(3)
