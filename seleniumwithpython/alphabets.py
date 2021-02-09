import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


def test_inputs_with_alphabets():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('http://the-internet.herokuapp.com/inputs')
    driver.find_element_by_xpath("//input[@type='number']").send_keys("AB")

    driver.close()