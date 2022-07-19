from selenium.webdriver.common.by import By
from simple_Project.locators import locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        # self.username_textbox_ID = "email"
        self.username_textbox_ID = locators.Locators.username_textbox_ID
        self.passward_textbox_Name = locators.Locators.passward_textbox_Name
        self.login_button_Name = locators.Locators.login_button_Name

    def enter_username(self, username):
        self.driver.find_element(By.NAME, locators.Locators.username_textbox_ID).clear()
        self.driver.find_element(By.NAME, self.username_textbox_ID).send_keys(username)

    def enter_passsward(self, passward):
        self.driver.find_element(By.NAME, self.passward_textbox_Name).clear()
        self.driver.find_element(By.NAME, self.passward_textbox_Name).send_keys(passward)

    def click_login(self):
        self.driver.find_element(By.NAME, self.login_button_Name).click()
