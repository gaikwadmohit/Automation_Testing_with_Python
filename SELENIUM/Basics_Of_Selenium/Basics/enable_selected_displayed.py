import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:

    def check_isenable_displayed_selected(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()

        e1=driver.find_element(By.ID,"sex-0")
        e1.click()
        print("Is male button displayed : : ", e1.is_displayed())
        print("Is male button enable : : ", e1.is_enabled())
        print("Is male button selected : : ", e1.is_selected())
        print("______________________")

        e2 = driver.find_element(By.ID, "sex-1")
        e2.click()

        print("Is female button displayed : : ",e2.is_displayed())
        print("Is female button enable : : ",e2.is_enabled())
        print("Is female button selected : : ",e2.is_selected())

        print("after click on female button male becomes deselect________________________")

        print("Is male button displayed after female select: : ",e1.is_displayed())
        print("Is male button enable after female select: : ",e1.is_enabled())
        print("Is male button selected after female select: : ",e1.is_selected())
        print("______________________")

        checkbox1 = driver.find_element(By.ID,"profession-0")
        checkbox1.click()
        select=(checkbox1.is_selected())
        print(select)

        checkbox1.click()
        if checkbox1.is_selected():
            print("Manual tester checkbox is selected")
        else:
            print("Manual tester checkbox isnot selected")




m = A()
m.check_isenable_displayed_selected()
