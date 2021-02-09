from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from tabletest import WebTable


def test_web_table():
        driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")
        driver.implicitly_wait(30)

        driver.get("http://the-internet.herokuapp.com/tables")
        w = WebTable(driver.find_element_by_xpath("//table[@id='table1']"))

        print("No of rows : ", w.get_row_count())
        print("------------------------------------")
        print("No of cols : ", w.get_column_count())
        print("------------------------------------")
        print("Table size : ", w.get_table_size())
        print("------------------------------------")
        print("First row data : ", w.row_data(1))
        print("------------------------------------")
        print("First column data : ", w.column_data(1))

        driver.close