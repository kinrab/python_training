# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
import unittest
import time


class UntitledTestCase(unittest.TestCase):

    def setUp(self):

        self.driver = WebDriver()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):

        driver = self.driver

        self.Open_Home_Page(driver)

        time.sleep(3)

        self.Login_process(driver)

        time.sleep(3)

        self.Show_Groups_List(driver)

        time.sleep(3)

        self.Add_New_Group(driver)

        self.Show_Groups_List(driver)

        time.sleep(3)

        self.Logout_process(driver)

        time.sleep(3)

    def Logout_process(self, driver):

        driver.find_element(By.LINK_TEXT, "Logout").click()

    def Add_New_Group(self, driver):

        driver.find_element(By.NAME, "new").click()

        time.sleep(3)

        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys("Test_group")

        time.sleep(3)

        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys("test_group_header")

        time.sleep(3)

        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys("test_group_footer")

        time.sleep(3)

        driver.find_element(By.NAME, "submit").click()

    def Show_Groups_List(self, driver):

        driver.find_element(By.LINK_TEXT, "groups").click()

    def Login_process(self, driver):

        # Ввод в поле логина admin
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").clear()
        driver.find_element(By.NAME, "user").send_keys("admin")

        # Ввод в поле пароля secret
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").clear()
        driver.find_element(By.NAME, "pass").send_keys("secret")

        time.sleep(3)

        # Нажать на кнопку Login
        driver.find_element(By.XPATH, "//input[@value='Login']").click()

    def Open_Home_Page(self, driver):

        driver.get("http://localhost:8080/addressbook/")

    def tearDown(self):

        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
