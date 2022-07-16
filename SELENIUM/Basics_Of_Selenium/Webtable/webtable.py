import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class webtable:
    def table(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("file:\\C:\\Users\\MOHIT\\table1.html")
        driver.maximize_window()
        time.sleep(3)

        #Print total no of rows,column and cells in table

        rows = (len(driver.find_elements(By.XPATH, "//tr")))
        print("rows: ",rows)

        columns = (len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")))
        print("columns :",columns)

        cells = str(len(driver.find_elements(By.XPATH, "//th|//td")))
        print("cells :",cells)
        print("*********************************************************")

        #print text
        text_data=driver.find_element(By.XPATH,"//table/tbody/tr[2]/td[2]").text
        print("from second row first column:",text_data)
        print("*********************************************************")

        #print all data from table
        for r in range(2,rows+1):
            for c in range(1,columns+1):
                text_data_all = driver.find_element(By.XPATH, "//table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                print(text_data_all)


    def table2_data(self):
        serv_obj = Service('C:\\Users\\MOHIT\\PycharmProjects\\SELENIUM\\Drivers\\chromedriver.exe')
        driver = webdriver.Chrome(service=serv_obj)
        driver.get("file:\\C:\\Users\\MOHIT\/table2.html")
        driver.maximize_window()
        time.sleep(3)

        rows = (len(driver.find_elements(By.XPATH, "//tr")))
        print("rows: ", rows)

        columns = (len(driver.find_elements(By.XPATH, "/html/body/table/tbody/tr[1]/th")))
        print("columns :", columns)

        # print all data from table
        for r in range(2, rows + 1):
            for c in range(1, columns + 1):
                text_data_all = driver.find_element(By.XPATH,
                                                    "//table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
                print(text_data_all)






obj = webtable()
# obj.table()
obj.table2_data()
