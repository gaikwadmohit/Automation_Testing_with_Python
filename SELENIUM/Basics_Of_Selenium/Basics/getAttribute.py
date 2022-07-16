import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class A:

    def check_getattribute(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()
        driver.implicitly_wait(10)

        e1 = driver.find_element(By.NAME,"firstname")
        e1.send_keys("Mohit")
        attribute=e1.get_attribute("name")

        if attribute=="firstname":
            print("Attribute value is correct")
        else:
            print("Attribute value isnot correct")


    def return_getproperty(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()
        driver.implicitly_wait(10)


        text = driver.find_element(By.XPATH,"//h3[@class='post-title entry-title']")
        print(text.tag_name)

        ele = text.get_property("text_length")
        print(ele)

        ele1 = text.get_property("property name")
        print(ele1)

    def return_value_of_CSS_property(self):
        serv_obj = Service('/Drivers/chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        driver.maximize_window()


        text = driver.find_element(By.XPATH,"//h3[@class='post-title entry-title']")
        print(text.value_of_css_property("font"))
        print(text.value_of_css_property("font-size"))
        print(text.value_of_css_property("letter-spacing"))
        print(text.value_of_css_property("text-align"))
        print(text.value_of_css_property("color"))






m = A()
# m.check_getattribute()
# m.return_getproperty()
m.return_value_of_CSS_property()



