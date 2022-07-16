import time
import unittest
from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        cls.driver = webdriver.Chrome(service=serv_obj)
        cls.driver.maximize_window()

    def test_search_bridgelabz(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME,"q").send_keys("Bridgelabz.com")
        self.driver.find_element(By.NAME,"btnK").click()
        time.sleep(3)

    def test_search_selenium(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME,"q").send_keys("Selenium with python")
        self.driver.find_element(By.NAME,"btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed....")


if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/MOHIT/PycharmProjects/Project_POM/Reports'))



