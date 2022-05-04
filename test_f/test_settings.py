from pages.settings_page import SettingsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date, datetime


def test_marketing_calendar(driver):
    settings_page = SettingsPage(driver)
    sleep(2)
    settings_page.marketing_calendar_dd.click()
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    settings_page.store_details_save.click()
    driver.refresh()
    sleep(2)
    assert "Human" in settings_page.marketing_calendar_dd.text
    sleep(2)
    settings_page.marketing_calendar_dd.click()
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_UP).send_keys(Keys.ENTER).perform()
    settings_page.store_details_save.click()
    driver.refresh()
    sleep(2)
    assert "5-4-4" in settings_page.marketing_calendar_dd.text


def test_calendar(driver):
    today = date.today()
    settings_page = SettingsPage(driver)
    settings_page.calendar_input_icon.click()
    day_10 = driver.find_element(By.CLASS_NAME, "react-datepicker__day--010")
    day_10.click()
    sleep(2)
    settings_page.store_details_save.click()
    driver.refresh()
    sleep(5)
    assert today == settings_page.calendar_input.get_attribute("value")


def test_timezone(driver):
    settings_page = SettingsPage(driver)
    sleep(2)
    settings_page.timezone_dd.click()
    ActionChains(driver).send_keys("min").send_keys(Keys.ENTER).perform()
    settings_page.store_details_save.click()
    driver.refresh()
    sleep(2)
    assert "(GMT+03:00) Europe/Minsk" in settings_page.timezone_dd.text
    sleep(2)
    settings_page.timezone_dd.click()
    ActionChains(driver).send_keys("lo").send_keys(Keys.ENTER).perform()
    settings_page.store_details_save.click()
    driver.refresh()
    sleep(2)
    assert "(GMT-00:00) Europe/London" in settings_page.timezone_dd.text


def test_notifications(driver):
    settings_page = SettingsPage(driver)
    sleep(2)
    driver.execute_script("arguments[0].click();", settings_page.notification_campaign_started)
    settings_page.notifications_save.click()
    driver.refresh()
    sleep(2)
    assert settings_page.notification_campaign_started.get_attribute("checked") == "true"
    driver.execute_script("arguments[0].click();", settings_page.notification_campaign_started)
    settings_page.notifications_save.click()
    driver.refresh()
    sleep(2)
    assert settings_page.notification_campaign_started.get_attribute("checked") is None


def test_add_team_member(driver):
    settings_page = SettingsPage(driver)
    sleep(2)
    driver.execute_script("arguments[0].click();", settings_page.add_team_member_plus)
    settings_page.add_team_member_input.click()
    driver.execute_script("arguments[0].value= 'qwe@qwe.com'", settings_page.add_team_member_input)
    settings_page.add_team_member_submit.click()
    driver.refresh()
    sleep(2)
    assert "qwe@qwe.com" in settings_page.team_member_block.text
    settings_page.team_member_trash_icon.click()
    settings_page.team_member_confirm_remove.click()
    driver.refresh()
    sleep(2)
    assert "qwe@qwe.com" not in settings_page.team_member_block.text


