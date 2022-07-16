import time
import unittest
import htmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.implicitly_wait(10)
        driver.maximize_window()

    def test_search_bridgelabz(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME,"q").send_keys("Bridgelabz.com")
        self.driver.find_element(By.NAME,"btnK").click()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


