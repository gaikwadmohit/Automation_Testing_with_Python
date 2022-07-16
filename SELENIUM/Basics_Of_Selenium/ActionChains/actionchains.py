import time

from select import select
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:

    def click_action(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.amazon.in")
        driver.maximize_window()

        a = driver.find_element(By.XPATH, "//*[@id='nav-xshop']/a[6] ")
        act = ActionChains(driver)
        act.click(a)
        act.perform()
        print(driver.title)

    def click_and_hold(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.amazon.in")
        driver.maximize_window()

        a = driver.find_element(By.XPATH, "//*[@id='nav-xshop']/a[7]")
        act = ActionChains(driver)
        act.click_and_hold(a)
        act.perform()
        time.sleep(4)
        print(driver.title)
        driver.close()

    def context_click_doubleclick(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.amazon.in")
        driver.maximize_window()

        a = driver.find_element(By.XPATH, "//*[@id='nav-xshop']/a[7]")
        act = ActionChains(driver)
        act.context_click(a)
        act.perform()
        time.sleep(4)

        a = driver.find_element(By.XPATH, "//*[@id='nav-xshop']/a[2]")
        act = ActionChains(driver)
        act.double_click(a).perform()
        time.sleep(4)
        print(driver.title)
        driver.close()

    def sendkeys(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.instagram.com/accounts/login/")
        driver.maximize_window()
        time.sleep(5)
        act = ActionChains(driver)
        a=driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        act.click(a).perform()
        time.sleep(5)
        act.send_keys_to_element(a, "Mohit").perform()

        time.sleep(5)

        print(driver.title)
        driver.close()

    def drag_and_drop(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://demos.telerik.com/kendo-ui/treeview/dragdrop")
        time.sleep(10)
        driver.maximize_window()

        act = ActionChains(driver)
        item1 = driver.find_element(By.XPATH, "//span[text()='Furniture']")

        time.sleep(3)
        target = driver.find_element(By.XPATH, "//span[text()='Floor Shelving']")

        act.drag_and_drop(item1,target).perform()
        time.sleep(10)
        driver.close()

    def mousehouver(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html")
        driver.maximize_window()

        movemouse = driver.find_element(By.XPATH, "//*[@id='post-body-4229879368008023176']/div[1]/div[2]/button")
        act = ActionChains(driver)
        act.move_to_element(movemouse).perform()
        time.sleep(5)
        appium_click=driver.find_element(By.XPATH, "//*[@id='post-body-4229879368008023176']/div[1]/div[2]/div/a[3]")
        appium_click.click()


        print(driver.title)
        driver.close()





m = A()
# m.click_action()
# m.click_and_hold()
# m.context_click_doubleclick()
# m.sendkeys()
# m.drag_and_drop()
# m.mousehouver()


