from selenium.webdriver.common.by import By
from simple_Project.locators import locators


class homepage():

    def __init__(self, driver):
        self.driver = driver

        self.create_story_logo = locators.Locators.create_story_logo
        self.create_text_story = locators.Locators.create_text_story
        self.logo_button_logo = locators.Locators.logo_button_logo
        self.logout_button_Link = locators.Locators.logout_button_Link

    def click_on_create_story(self):
        self.driver.find_element(By.XPATH, self.create_story_logo).click()
        self.driver.find_element(By.LINK_TEXT, self.create_text_story).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH, self.logo_button_logo).click()
        self.driver.find_element(By.XPATH, self.logout_button_Link).click()
