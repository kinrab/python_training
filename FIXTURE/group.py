
from selenium.webdriver.common.by import By
import time

class GroupHelper:

    def __init__(self, app):

        self.app = app


    def Add_New_Group(self, group):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(3)

        driver.find_element(By.NAME, "new").click()

        time.sleep(3)

        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(group.group_name)

        time.sleep(3)

        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").clear()
        driver.find_element(By.NAME, "group_header").send_keys(group.group_header)

        time.sleep(3)

        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").clear()
        driver.find_element(By.NAME, "group_footer").send_keys(group.group_footer)

        time.sleep(3)

        driver.find_element(By.NAME, "submit").click()

        self.Show_Groups_List()
        time.sleep(3)

    def Show_Groups_List(self):

        driver = self.app.driver

        driver.find_element(By.LINK_TEXT, "groups").click()

    def Delete_First_Group (self):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(3)

        # Выбрать первый по списку чек-бокс
        driver.find_element(By.NAME, "selected[]").click()

        # Нажать на кнопку Delete
        driver.find_element(By.NAME, "delete").click()
        time.sleep(3)

        self.Show_Groups_List()
        time.sleep(3)

    def Edit_First_Group(self):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(3)

        # Выбрать первую в списке групу - check box activate
        driver.find_element(By.NAME, "selected[]").click()

        # Нажать кнопку Edit
        driver.find_element(By.NAME, "edit").click()

        # В открывшемся окне добавить в название группы какой-то символ
        item = driver.find_element(By.NAME, "group_name")
        val = item.get_attribute("value")

        print(" Исходное значение: {  "+ val + " }")

        val = val + "(*)"

        print("Новое значение: {  "+ val + " }")

        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").clear()
        driver.find_element(By.NAME, "group_name").send_keys(val)

        time.sleep(3)

        # Нажать на кнопку Update
        driver.find_element(By.NAME, "update").click()

        time.sleep(3)

        # Открыть список групп

        self.Show_Groups_List()
        time.sleep(3)

