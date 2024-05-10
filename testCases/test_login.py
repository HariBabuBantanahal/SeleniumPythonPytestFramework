import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage

@allure.severity(allure.severity_level.MINOR)
class Test_001_Login:
    baseURL="https://admin-demo.nopcommerce.com/"
    username="admin@yourstore.com"
    password="admin"

    @allure.severity(allure.severity_level.MINOR)
    def test_HomePageTitle(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:

            assert False
            self.driver.close()
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self , setup):
        self.driver = setup
        self.lp=LoginPage(self.driver)
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)

        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.driver.maximize_window()
        act_val= self.lp.driver.title
        if act_val == "Dashboar / nopCommerce administration":
            self.lp.driver.close()
            assert True
        else:
            self.lp.driver.save_screenshot(".\\saveScreenshots\\" + "test_login.png")
            allure.attach(self.driver.get_screenshot_as_png(),name = "Login Homepage",attachment_type=AttachmentType.PNG)
            self.lp.driver.close()
            assert False







