import time
from unittest import TestCase

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import unittest
# import os
# import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), "...","..."))
from simple_Project.Page.loginpage import LoginPage
from simple_Project.Page.homepage import homepage


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        # driver.get("https://parabank.parasoft.com/parabank/index.htmc")
        driver.get("https://www.facebook.com/")

        login=LoginPage(driver)
        login.enter_username("8668242077")
        login.enter_passsward("G@ikwadMohit")
        login.click_login()

        home_page=homepage(driver)
        home_page.click_on_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test successfully done")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/MOHIT/PycharmProjects/Project_POM2/simple_Project/Reports'))
