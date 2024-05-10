from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id="Email"
    textbox_password_id="Password"
    btn_login_xpath = "//button[@type='submit']"
    btn_logout_linktext = "Logout"

    # Action Method
    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickLogut(self):
        self.driver.find_element(By.LINK_TEXT,self.btn_login_xpath).click()
