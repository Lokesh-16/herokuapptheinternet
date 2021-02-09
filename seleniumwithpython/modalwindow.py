import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from time import sleep


def test_modal_window():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('https://the-internet.herokuapp.com/entry_ad')

    parent_h = driver.current_window_handle
    driver.switch_to.window(parent_h)
    driver.find_element_by_xpath("//div[@class='modal-footer']/p").click()
    driver.switch_to.window(parent_h)

    sleep(5)

    driver.close()