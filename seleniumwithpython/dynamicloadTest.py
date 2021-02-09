

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from time import sleep

def test_dynamic_loading():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')

    driver.find_element_by_xpath("//div[@id='start']/button").click()
    sleep(10)

    textin = driver.find_element_by_css_selector('h4').text
    assert 'Hello World!' == driver.find_element_by_xpath("//div[@id='finish']/h4").text


    driver.close()