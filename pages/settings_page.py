from pages.base_page import BasePage
from selenium.webdriver.common.by import By


store_details_actions_block = (By.CLASS_NAME, "str-details__store-sets")
drop_downs = (By.CLASS_NAME, "css-1uccc91-singleValue")
calendar_input_icon = (By.CLASS_NAME, "calendar-input__icon")
calendar_input = (By.CLASS_NAME, "custom-date-picker__input")
save_buttons = (By.CLASS_NAME, "settings-pg__save-btn")
notification_campaign_started = (By.ID, "campaignStarted")
add_team_member_plus_icon = (By.CLASS_NAME, "team-form__add-user")
add_team_member_input = (By.ID, "email")
add_team_member_submit = (By.CLASS_NAME, "team-form__submit-icon")
team_member_block = (By.CLASS_NAME, "settings-pg__team-block")
team_member_trash_icon = (By.CLASS_NAME, "team-form__trash-btn")
team_member_confirm_remove = (By.CSS_SELECTOR, "body > div:nth-child(12) > div > div > div.confirmation-modal__action-block > button.custom-button.confirmation-modal__btn.primary")


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @property
    def store_details_actions_block(self):
        return self.find_element(store_details_actions_block)

    @property
    def marketing_calendar_dd(self):
        return self.find_elements(drop_downs)[1]

    @property
    def calendar_input_icon(self):
        return self.find_element(calendar_input_icon)

    @property
    def calendar_input(self):
        return self.find_element(calendar_input)

    @property
    def timezone_dd(self):
        return self.find_elements(drop_downs)[2]

    @property
    def store_details_save(self):
        return self.find_elements(save_buttons)[1]

    @property
    def notification_campaign_started(self):
        return self.find_element(notification_campaign_started)

    @property
    def notifications_save(self):
        return self.find_elements(save_buttons)[2]

    @property
    def add_team_member_plus(self):
        return self.find_element(add_team_member_plus_icon)

    @property
    def add_team_member_input(self):
        return self.find_elements(add_team_member_input)[1]

    @property
    def add_team_member_submit(self):
        return self.find_element(add_team_member_submit)

    @property
    def team_member_block(self):
        return self.find_element(team_member_block)

    @property
    def team_member_trash_icon(self):
        return self.find_element(team_member_trash_icon)

    @property
    def team_member_confirm_remove(self):
        return self.find_element(team_member_confirm_remove)
