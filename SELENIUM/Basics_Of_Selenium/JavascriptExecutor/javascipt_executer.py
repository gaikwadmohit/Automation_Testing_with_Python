import time

from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:

    def js_click_title_refresh_alert_docRead(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.amazon.in/")
        driver.maximize_window()


        # a=driver.find_element(By.XPATH,"//*[@id='nav-xshop']/a[2]")
        # driver.execute_script("arguments[0].click();", a)

        #return title of web page
        # title = driver.execute_script("return document.title;")
        # print(title)

        #to refresh a page after 2 sec
        # time.sleep(2)
        # driver.execute_script("history.go(0);")

        #alert pop up
        # time.sleep(5)
        # driver.execute_script("alert('Hello Mohit');")

        #Return document whole text
        # doc=driver.execute_script("return document.documentElement.innerText;")
        # print(doc)

        #Border to element
        time.sleep(5)
        highlight_border=driver.find_element(By.PARTIAL_LINK_TEXT,"Customer Service")
        driver.execute_script("argument[0].style.border = '3px solid red'",highlight_border)
        time.sleep(3)

        driver.close()

    def js_border(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.facebook.com/")
        driver.maximize_window()

        highlight=driver.find_element(By.XPATH,"//*[@id='passContainer']")
        driver.execute_script("arguments[0].style.border ='3px solid red'", highlight)
        time.sleep(5)
        driver.close()
        time.sleep(5)

    def scroll_down(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.amazon.in/")
        driver.maximize_window()

        # scroll_upto_starthere=driver.find_element(By.XPATH,"//span[@class='navFooterBackToTopText']")
        # driver.execute_script("arguments[0].scrollIntoView(true);", scroll_upto_starthere)
        # time.sleep(5)

        #return user agent information
        # print(driver.execute_script(("return navigator.userAgent;")))
        # driver.close()


        #scroll to bottom of page and return top of page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(document.body.scrollHeight , 0)")
        time.sleep(2)











m = A()
# m.js_click_title_refresh_alert_docRead()
# m.js_border()
m.scroll_down()