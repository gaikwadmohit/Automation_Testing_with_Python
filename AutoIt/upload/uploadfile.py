import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


class A:
    def uploadfile(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://document.online-convert.com/convert-to-pdf")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div[1]/div/div/div/button').click()
        time.sleep(3)
        release_file = r"C:/Users/MOHIT/OneDrive/Desktop/AutoIT/upload.exe"
        os.system(release_file)

        time.sleep(3)


o = A()
o.uploadfile()
