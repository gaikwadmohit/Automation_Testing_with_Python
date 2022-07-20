import time
from selenium.webdriver.common.by import By
from simple_Project.locators import locators


class profilepage():

    def __init__(self, driver):
        self.driver = driver

        self.click_on_profilename = locators.Locators.click_on_profilename
        self.post = locators.Locators.click_on_post
        self.about = locators.Locators.click_on_about
        self.click_on_friends = locators.Locators.click_on_friends
        self.click_on_photos = locators.Locators.click_on_photos
        self.click_on_videos = locators.Locators.click_on_videos
        self.click_on_checkin = locators.Locators.click_on_checkin
        self.select_home_logo1 = locators.Locators.select_home_logo1

    def profileElements(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_profilename).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.post).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.about).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_friends).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_photos).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_videos).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.click_on_checkin).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.select_home_logo1).click()
        time.sleep(3)

