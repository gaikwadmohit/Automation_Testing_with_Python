import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:

    def handling_frame(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
        driver.maximize_window()

        driver.switch_to.frame("packageListFrame")
        driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
        driver.switch_to.default_content()

        driver.switch_to.frame("packageFrame")
        driver.find_element(By.LINK_TEXT,"Alert").click()
        driver.switch_to.default_content()

        time.sleep(2)

        driver.switch_to.frame("classFrame")
        driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()







m = A()
m.handling_frame()