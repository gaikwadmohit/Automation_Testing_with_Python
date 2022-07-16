import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:
    def ALERT_POPUP(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@name='alert']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)

    def confirmation_popup(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()

        driver.get("https://nxtgenaiacademy.com/alertandpopup/")
        driver.find_element(By.XPATH, "//button[@name ='confirmalertbox']").click()
        time.sleep(5)
        alert = driver.switch_to.alert
        time.sleep(5)
        txt = alert.text
        print(txt)
        alert.accept()
        time.sleep(3)
        driver.close()


    def prompt_popup(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
        driver.find_element(By.XPATH, "//input[@name ='prompt']").click()
        time.sleep(5)
        alert = driver.switch_to.alert
        time.sleep(5)
        a = alert.text
        print(a)
        alert.accept()
        driver.close()

    def upload_file(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get("https://nervgh.github.io/pages/angular-file-upload/examples/simple/")
        driver.find_element(By.XPATH, "//input[@multiple ='']").send_keys("C:\\Users\\MOHIT\\table1.html")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@ng-click=\"item.upload()\"]")
        time.sleep(5)


    def download_file(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        # serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\msedgedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.maximize_window()
        driver.get("https://www.selenium.dev/downloads/")
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, '32 bit Windows IE').click()
        time.sleep(6)
        driver.close()

obj = A()
obj.ALERT_POPUP()
# obj.upload_file()
# obj.prompt_popup()
# obj.confirmation_popup()
# obj.download_file()
