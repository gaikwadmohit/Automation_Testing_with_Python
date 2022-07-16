# import time
#
# import pytest
# from select import select
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver=None
# @pytest.fixture
# def setup():
#     print("Start Browser")
#     global driver
#     serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
#     driver = webdriver.Chrome(service=serv_obj)
#     driver.maximize_window()
#     yield
#     driver.quit()
#     print("Close browser")
#
# def test1(setup):
#     driver.get("https://www.facebook.com/")
#     print("test 1 executed")
#
#
# def test2(setup):
#     driver.get("https://www.google.com/")
#     print("test 2 executed")
#
# def test3(setup):
#     driver.get("https://www.gmail.com/")
#     print("test 3 executed")