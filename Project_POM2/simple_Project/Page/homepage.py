from selenium.webdriver.common.by import By
from simple_Project.locators import locators

class homepage():

    def __init__(self,driver):
        self.driver=driver

        self.logo_button_logo   = locators.Locators.logo_button_logo
        self.logout_button_Link = locators.Locators.logout_button_Link


    def click_on_logout(self):

        self.driver.find_element(By.XPATH, self.logo_button_logo).click()

        self.driver.find_element(By.XPATH, self.logout_button_Link).click()

