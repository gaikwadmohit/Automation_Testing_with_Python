import time
from selenium import webdriver
from selenium.webdriver.chrome.service import   Service
from selenium.webdriver.common.by import By

serv_obj=Service('/Drivers/chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.in/")
driver.maximize_window()


# driver.get("https://www.facebook.com/")
# time.sleep(4)
# driver.back()
# time.sleep(4)
# driver.forward()
print("______________________________________________")

# tit=driver.title
# print(tit)
#print("______________________________________________")

# nam=driver.name
# print(nam)
#print("______________________________________________")

# url=driver.current_url
# print(url)
# print("______________________________________________")

# driver.fullscreen_window()
# driver.refresh()
# print(driver.page_source)
# print("______________________________________________")

# driver.save_screenshot("mohit.png")
# print(driver.get_screenshot_as_png())

# print(driver.get_window_size())



driver.close()
