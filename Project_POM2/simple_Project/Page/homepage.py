import time

from selenium.webdriver.common.by import By
from simple_Project.locators import locators


class homepage():

    def __init__(self, driver):
        self.driver = driver
        self.select_home_logo = locators.Locators.select_home_logo
        self.click_photo_video = locators.Locators.click_photo_video
        self.click_emoji = locators.Locators.click_emoji
        self.click_on_happy = locators.Locators.click_on_happy
        self.click_on_post_button = locators.Locators.click_on_post_button


    def start_with_homepage(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.select_home_logo).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.click_photo_video).click()
        self.driver.find_element(By.XPATH,self.click_emoji).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.click_on_happy).click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,self.click_on_post_button).click()
        time.sleep(4)




