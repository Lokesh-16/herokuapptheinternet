import pytest

from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from time import sleep


def test_file_Upload():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('https://the-internet.herokuapp.com/upload')
    uploadfile = driver.find_element_by_xpath("//input[@id='file-upload']")
    uploadfile.send_keys("C:\logo.png")
    driver.find_element_by_xpath("//input[@value='Upload']").click()

    sleep(5)

    textin = driver.find_element_by_css_selector('h3').text
    assert 'File Uploaded!' == driver.find_element_by_xpath("//div[@class='example']/h3").text
    driver.close()