import time

from selenium import webdriver
from selenium.webdriver.chrome.service import   Service
from selenium.webdriver.common.by import By
serv_obj=Service('/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.amazon.in/")
driver.maximize_window()

# driver.find_element(By.ID,'twotabsearchtextbox').send_keys("shirt for men stylish latest 2022")
# driver.find_element(By.ID,"nav-search-submit-button").click()

txt=driver.find_element(By.XPATH,"//a[@class='nav-logo-link nav-progressive-attribute']")
print(txt)

# driver.find_element(By.XPATH,"//span[contains(text(),'Select your address')]").click()
# time.sleep(4)





driver.close()