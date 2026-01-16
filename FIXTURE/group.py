
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

        self.Fill_Group_Form(group)

        time.sleep(3)

        driver.find_element(By.NAME, "submit").click()

        self.Show_Groups_List()
        time.sleep(3)

    def Change_Field_Value(self, text, group_item):

        driver = self.app.driver

        if text is not None:

            driver.find_element(By.NAME, group_item).click()
            driver.find_element(By.NAME, group_item).clear()
            driver.find_element(By.NAME, group_item).send_keys(text)
            time.sleep(3)

    def Fill_Group_Form(self, group):

        self.Change_Field_Value(group.group_name, "group_name")

        self.Change_Field_Value(group.group_header, "group_header")

        self.Change_Field_Value(group.group_footer, "group_footer")


    def Show_Groups_List(self):

        driver = self.app.driver

        driver.find_element(By.LINK_TEXT, "groups").click()


    def Delete_First_Group (self):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(3)

        self.Select_First_Group()

        # Нажать на кнопку Delete
        driver.find_element(By.NAME, "delete").click()
        time.sleep(3)

        self.Show_Groups_List()
        time.sleep(3)


    def Edit_First_Group(self):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(3)

        self.Select_First_Group()

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


    def Modify_First_Group(self, new_group_data):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(3)

        self.Select_First_Group()

        # Open modification form
        driver.find_element(By.NAME, "edit").click()

        # Fill the form
        self.Fill_Group_Form(new_group_data)

        # Submit midification
        driver.find_element(By.NAME, "update").click()

        # Вернуться к списку групп
        self.Show_Groups_List()
        time.sleep(3)

    def Select_First_Group(self):

        driver = self.app.driver

        # Выбрать первый по списку чек-бокс

        driver.find_element(By.NAME, "selected[]").click()