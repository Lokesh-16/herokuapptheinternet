import pytest

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

def test_drop_down():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('https://the-internet.herokuapp.com/dropdown')
    driver.get_screenshot_as_file("some.png")
    driver.find_element_by_xpath("(//select[@id='dropdown'])/option[@value='2']").click()
    driver.get_screenshot_as_file("screenshot.png")

    driver.close()
