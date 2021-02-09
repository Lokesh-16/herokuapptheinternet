import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from time import sleep

def test_log_in():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element_by_id('username').send_keys('tomsmith')
    driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
    driver.find_element_by_xpath("//button[@type='submit']").click()

    assert 'Welcome to the Secure Area. When you are done click logout below.' == driver.find_element_by_xpath("//h4[@class='subheader']").text


    sleep(5)

    driver.close()