import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import allure
from allure import attachment_type

@allure.severity(allure.severity_level.MINOR)
class Test_Allure_report:
    def test_amazone_web(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.in/")
        time.sleep(3)

        logo_dispayed = self.driver.find_element(By.XPATH, "//*[@id='nav-logo-sprites']").is_displayed()
        if logo_dispayed == True:
            assert True
            print("Logo is available")
        else:
            assert False

        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_best_seller(self):

        pytest.skip("i am skipping this method, i will do it letter")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        self.driver = webdriver.Chrome(service=serv_obj)
        self.driver.maximize_window()
        self.driver.get("https://www.amazon.in/")
        time.sleep(3)

        self.driver.find_element(By.XPATH, "//*[@id='nav-link-accountList-nav-line-1']").click()
        self.driver.find_element(By.XPATH, "//*[@id='ap_email']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='ap_email']").send_keys("918482943335")
        self.driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='ap_password']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='ap_password']").send_keys("gaikwad595")
        self.driver.find_element(By.XPATH, "//*[@id='signInSubmit']").click()

        act_title=self.driver.title
        if act_title==True:
            print(self.driver.title)
            allure.attach(allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=attachment_type.PNG))
        else:
            self.driver.close()


