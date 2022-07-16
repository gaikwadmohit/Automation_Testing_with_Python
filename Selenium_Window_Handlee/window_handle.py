import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class A:
    def multiple_window(self):
        # ops = webdriver.ChromeOptions()
        # ops.headless = True
        # ops.add_argument("--disable-notifications")  #to disable popups
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        # driver = webdriver.Chrome(service=serv_obj, options=ops)
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.naukri.com/")
        driver.maximize_window()
        time.sleep(5)

        parent_window = driver.current_window_handle
        print("windowid of parent :----",parent_window)
        driver.find_element(By.LINK_TEXT,"Companies").click()
        time.sleep(5)
        print("title of parent page:-----",driver.title)
        all_handles = driver.window_handles

        for handles in all_handles:
            if handles != parent_window:
                driver.switch_to.window(handles)
                time.sleep(5)
                driver.find_element(By.LINK_TEXT, "3D PLM Software Jobs").click()
                print("title of child page :----", driver.title)
                time.sleep(5)
                print("windowid :----", all_handles)
                break


        driver.switch_to.window(parent_window)
        time.sleep(5)

        #click on register now button
        driver.find_element(By.CLASS_NAME,"singleSelectChip").click()

        time.sleep(10)
        driver.close()


a=A()
a.multiple_window()