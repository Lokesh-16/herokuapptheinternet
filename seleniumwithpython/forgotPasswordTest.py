import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from time import sleep

def test_forgotPassword():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('http://the-internet.herokuapp.com/forgot_password')

    driver.find_element_by_xpath("//input[@id='email']").send_keys("lokeshn@gmail.com")
    driver.find_element_by_id('form_submit').click()

    textin = driver.find_element_by_xpath("//div[@id='content']").text
    assert 'Your e-mail\'s been sent!' == driver.find_element_by_xpath("//div[@id='content']").text

    driver.get('http://the-internet.herokuapp.com/login')
    driver.find_element_by_id('username').send_keys('tomsmith')
    driver.find_element_by_id('password').send_keys('SuperSecretPassword!')
    driver.find_element_by_xpath("//button[@type='submit']").click()

    assert 'You logged into a secure area!' == driver.find_element_by_class_name('flash success').text


    sleep(5)

    driver.close()