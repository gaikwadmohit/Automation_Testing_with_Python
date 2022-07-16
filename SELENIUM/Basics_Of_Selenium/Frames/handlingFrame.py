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
        driver.get("https://chercher.tech/practice/frames-example-selenium-webdriver")
        driver.maximize_window()

        driver.switch_to.frame("frame1")
        driver.switch_to.frame("frame3")
        innerframe=driver.find_element(By.XPATH,"//*[@id='a']").click()
        # driver.switch_to.parent_frame()
        driver.switch_to.default_content()

        time.sleep(3)


        driver.switch_to.frame("frame2")
        a=Select(driver.find_element(By.ID,"frame2"))
        a.select_by_visible_text("Big Baby Cat")










m = A()
m.handling_frame()