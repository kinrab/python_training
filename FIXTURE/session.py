
from selenium.webdriver.common.by import By
import time

class SessionHelper:

    def __init__(self,app):

        self.app = app

    def Open_Home_Page(self):

        driver = self.app.driver

        driver.get("http://localhost:8080/addressbook/")

    def Login_process(self, username, password):

        driver = self.app.driver

        self.Open_Home_Page()
        time.sleep(3)

        # Ввод в поле логина admin
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)

        # Ввод в поле пароля secret
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)

        time.sleep(3)

        # Нажать на кнопку Login
        driver.find_element(By.XPATH, "//input[@value='Login']").click()


    def Logout_process(self):

        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()