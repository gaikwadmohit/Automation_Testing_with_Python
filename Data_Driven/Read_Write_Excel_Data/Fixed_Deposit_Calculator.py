import time
import XlUtils.xlutils
from XlUtils import xlutils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
driver = webdriver.Chrome(service=serv_obj)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('disable-notifications')
driver = webdriver.Chrome('chromedriver.exe', options=chrome_options)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = 'C:/Users/MOHIT/OneDrive/Desktop/simpla_data_read.xlsx'
rows = xlutils.getRowCount(file, "moneycontrol")

# Read data from Excel
for r in range(2, rows + 1):
    principle_amt = xlutils.readData(file, "moneycontrol", r, 1)
    rate_of_intrest = xlutils.readData(file, "moneycontrol", r, 2)
    period1 = xlutils.readData(file, "moneycontrol", r, 3)
    period2 = xlutils.readData(file, "moneycontrol", r, 4)
    frequency = xlutils.readData(file, "moneycontrol", r, 5)
    exp_maturity_value = xlutils.readData(file, "moneycontrol", r, 6)

    # Locate the element
    driver.find_element(By.XPATH, '//*[@id="principal"]').send_keys(principle_amt)
    driver.find_element(By.XPATH, '//*[@id="interest"]').send_keys(rate_of_intrest)
    driver.find_element(By.XPATH, '//*[@id="tenure"]').send_keys(period1)
    period_drop = Select(driver.find_element(By.XPATH, '//*[@id="tenurePeriod"]'))
    period_drop.select_by_visible_text(period2)
    freq_dropdown = Select(driver.find_element(By.XPATH, '//*[@id="frequency"]'))
    freq_dropdown.select_by_visible_text(frequency)
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_maturity = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text



    if float(act_maturity) == float(exp_maturity_value):
        print("Test Passed")
        xlutils.writeDta(file, "moneycontrol", r, 8, "passed")
        xlutils.fileGreenColor(file, "moneycontrol", r, 8)

    else:
        print("Test Failed")
        xlutils.writeDta(file, "moneycontrol", r, 8, "Failed")
        xlutils.fileRedColor(file, "moneycontrol", r, 8)

    # clear data
    driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)
driver.close()
