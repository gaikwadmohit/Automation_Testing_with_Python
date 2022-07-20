from selenium.webdriver.common.by import By
from simple_Project.locators import locators


class storyPage():

    def __init__(self, driver):
        self.driver = driver

        self.create_text_story = locators.Locators.create_text_story
        self.text_area = locators.Locators.text_area
        self.style_selection = locators.Locators.style_selection
        self.select_font = locators.Locators.select_font
        self.select_background = locators.Locators.select_background
        self.share_story = locators.Locators.share_story
        self.logo_button_logo = locators.Locators.logo_button_logo
        self.logout_button_Link = locators.Locators.logout_button_Link

    def write_story(self, text_for_story):
        self.driver.find_element(By.LINK_TEXT, self.create_text_story).click()
        self.driver.find_element(By.XPATH, self.text_area).send_keys(text_for_story)

    def select_design(self):
        self.driver.find_element(By.XPATH, self.style_selection).click()
        self.driver.find_element(By.XPATH, self.select_font).click()
        self.driver.find_element(By.XPATH, self.select_background).click()

    def send_story(self):
        self.driver.find_element(By.LINK_TEXT, self.share_story).click()

    def click_on_logout(self):
        self.driver.find_element(By.XPATH, self.logo_button_logo).click()
        self.driver.find_element(By.XPATH, self.logout_button_Link).click()

