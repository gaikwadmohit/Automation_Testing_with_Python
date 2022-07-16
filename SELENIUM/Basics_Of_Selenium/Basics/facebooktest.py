import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service('/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

# --------------Taking sreenshot of statement-------------------------------------
# driver.find_element(By.XPATH,"//h2[contains(text(),'Facebook helps you connect and share with the people in your life.')]").screenshot("fb.png")

# ----------------Useer id and passward-----------------
# user=driver.find_element(By.CSS_SELECTOR, "input#email")
# user.clear()
# user.send_keys("mohitgaikwad@gmail.com")
#
# passward=driver.find_element(By.CSS_SELECTOR,"input#pass")
# passward.clear()
# passward.send_keys("G@ikMani123")
#
# driver.find_element(By.NAME,"login").click()

# -----------------no of links--------------------

# link=driver.find_elements(By.TAG_NAME,"a")
# for i in link:
#     print(i.text)
#     print(i.size)


ALL_LINKS=driver.find_elements(By.TAG_NAME,"a")
print("Total no of links",len(ALL_LINKS))
for i in ALL_LINKS:
    print(i.text)




#--------------facebook signup-------------------
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Create New Account").click()
time.sleep(2)
driver.find_element(By.NAME,"firstname").send_keys("Mohit")
driver.find_element(By.NAME,"lastname").send_keys("Gaikwad")

driver.find_element(By.CSS_SELECTOR,"input[name='reg_email__']").send_keys("5588669988")


date=Select(driver.find_element(By.XPATH,"//select[@id='day]"))
date.select_by_value("10")








# driver.close()
