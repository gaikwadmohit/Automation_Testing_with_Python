import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:

    def check_alignment(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()

        fname_location = driver.find_element(By.NAME, "firstname")
        l1 = fname_location.size
        print(l1)

        lname_location = driver.find_element(By.NAME, "lastname")
        l2 = lname_location.size
        print(l2)

        if l1==l2:
            print("both text boxex aligned on same line")
        else:
            print("both text boxex not aligned on same line")


m = A()
m.check_alignment()
