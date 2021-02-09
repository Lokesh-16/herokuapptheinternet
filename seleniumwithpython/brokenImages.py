import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys

from time import sleep


def test_broken_Images():
    driver = webdriver.Chrome("C:\drivers\chromedriver_win32 (1)\chromedriver.exe")

    driver.get('https://the-internet.herokuapp.com/broken_images')
    images = driver.find_element_by_xpath("//div[@class='example']/img[3]")
    main_window = driver.current_window_handle
    action =ActionChains(driver)
    action.context_click(images).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    driver.switch_to.window()
    string = driver.find_element_by_css_selector('body > h1').text
    if string == 'Not Found':
        print("Selected image is broken")
    else:
        print ("Selected image is not broken")
    sleep(5)
    driver.switch_to.window(main_window)

    driver.close()