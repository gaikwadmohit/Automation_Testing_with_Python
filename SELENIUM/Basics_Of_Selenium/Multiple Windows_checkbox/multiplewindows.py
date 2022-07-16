import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class A:
    def multiple_window(self):
        # ops = webdriver.ChromeOptions()
        # ops.headless = True
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        # driver = webdriver.Chrome(service=serv_obj, options=ops)
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(5)

        parent_window = driver.current_window_handle
        print(parent_window)
        driver.find_element(By.XPATH,'//*[@id="yt_business_link"]/a/text()').click()
        time.sleep(5)
        all_handles = driver.window_handles
        print(all_handles)

        for handles in all_handles:
            if handles != parent_window:
                driver.switch_to.window(handles)

                driver.find_element(By.XPATH, "//*[@id='__next']/header/div/div/section/aside/nav[2]/a/span").click()
                time.sleep(5)
                driver.close()
                time.sleep(2)
                break
        driver.switch_to.window(parent_window)
        driver.find_element(By.XPATH, '//*[@id="booking_engine_hotels"]/span').click()

        time.sleep(10)
        driver.close()

    def multiple_checkbox(self):

        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("file:///C:/Users/MOHIT/table3.html")
        driver.maximize_window()
        time.sleep(5)

        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        time.sleep(2)
        for checkbox in checkboxes:
            if checkbox == checkboxes[0]:
                checkbox.click()
                time.sleep(2)


    def window_handle(self):
        # ops = webdriver.ChromeOptions()
        # ops.headless = True
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        # driver = webdriver.Chrome(service=serv_obj, options=ops)
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("http://demo.automationtesting.in/Windows.html")
        driver.maximize_window()
        time.sleep(5)

        driver.find_element(By.XPATH,"//*[@id='Tabbed']/a/button").click()
        print(driver.current_window_handle)
        print("Parent window title = ", driver.title)

        handles = driver.window_handles
        time.sleep(2)
        driver.switch_to.window(handles.__getitem__(1))
        print("First window after switching=", driver.title)
        time.sleep(2)

        driver.find_element(By.LINK_TEXT,("Downloads")).click()

        driver.switch_to.window(handles.__getitem__(0))
        driver.find_element(By.XPATH,("//*[@id='Tabbed']/a/button")).click()
        time.sleep(2)

        handles = driver.window_handles
        driver.switch_to.window(handles.__getitem__(2))
        print("Second window=", driver.title)

        time.sleep(3)

        driver.quit()


obj = A()
# obj.multiple_window()
obj.multiple_checkbox()
# obj.window_handle()
