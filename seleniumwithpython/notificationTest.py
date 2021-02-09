import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

from selenium.webdriver.support.select import Select


def assertTrue(param):
    pass


def test_lambdatest_todo_app():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('http://the-internet.herokuapp.com/notification_message_rendered')

    success = False
    while not success:
        driver.find_element_by_link_text('Click here').click()
        success = driver.find_element_by_xpath("//div[@id='flash']").is_displayed()
        failure = driver.find_element_by_xpath("//div[@id='flash']").is_displayed()
        assertTrue(failure or success)

    driver.close()