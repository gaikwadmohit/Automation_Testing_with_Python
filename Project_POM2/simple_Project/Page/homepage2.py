import time

from selenium.webdriver.common.by import By
from simple_Project.locators import locators


class homepage2():

    def __init__(self, driver):
        self.driver = driver
        self.click_on_findFriends = locators.Locators.click_on_findFriends
        self.click_on_menuBox = locators.Locators.click_on_menuBox
        self.click_on_masanger = locators.Locators.click_on_masanger
        self.click_on_notification = locators.Locators.click_on_notification
        self.logo_button_logo = locators.Locators.logo_button_logo
        self.logout_button_Link = locators.Locators.logout_button_Link

    def end_with_homepage2(self):
        self.driver.find_element(By.XPATH, self.click_on_findFriends).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_on_menuBox).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_on_masanger).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.click_on_notification).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.logo_button_logo).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.logout_button_Link).click()
