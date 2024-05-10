from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
import pytest

@pytest.fixture()
def setup():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach",True)
    driver = webdriver.Chrome(opt)
    return driver

