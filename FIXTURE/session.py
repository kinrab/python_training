
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

        # Открыть страницу приложения!
        self.Open_Home_Page()

        # Ввод в поле логина admin
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys(username)

        # Ввод в поле пароля secret
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys(password)

        # Нажать на кнопку Login
        driver.find_element(By.XPATH, "//input[@value='Login']").click()


    def Logout_process(self):

        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "Logout").click()


    def Ensure_Logout_process(self):

        #driver = self.app.driver

        if  self.Is_Logged_In():

            self.Logout_process()


    def Is_Logged_In(self):

        #print("Is_Logged_In:\n ")

        driver = self.app.driver

        num = len( driver.find_elements(By.LINK_TEXT, "Logout") )

        #print("Num = ", str(num) )

        return num > 0


    def Is_Logged_In_As(self, username):

        driver = self.app.driver

        item = driver.find_element(By.XPATH, "//div/div[1]/form/b")

        #print("Item: " + item.text + "\n" )

        return  item.text == "(" + username+ ")"


    def Ensure_Login_process(self, username, password):

        # Открыть страницу приложения!
        self.Open_Home_Page()

        Flag = self.Is_Logged_In()

        if  Flag is True:

            if self.Is_Logged_In_As(username):
                return
            else:
                self.Logout_process()

        self.Login_process(username,password)





