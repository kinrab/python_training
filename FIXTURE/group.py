
from selenium.webdriver.common.by import By
from MODEL.group import Group

import time

class GroupHelper:

    def __init__(self, app):

        self.app = app


    def Add_New_Group(self, group):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(1)

        driver.find_element(By.NAME, "new").click()

        time.sleep(1)

        self.Fill_Group_Form(group)

        time.sleep(1)

        driver.find_element(By.NAME, "submit").click()

        self.Show_Groups_List()
        time.sleep(1)

        self.group_cash = None # Кэш не валиден после добавлени, модификации, удаления групп

    def Change_Field_Value(self, text, group_item):

        driver = self.app.driver

        if text is not None:

            driver.find_element(By.NAME, group_item).click()
            driver.find_element(By.NAME, group_item).clear()
            driver.find_element(By.NAME, group_item).send_keys(text)
            time.sleep(1)

    def Fill_Group_Form(self, group):

        self.Change_Field_Value(group.group_name, "group_name")

        self.Change_Field_Value(group.group_header, "group_header")

        self.Change_Field_Value(group.group_footer, "group_footer")


    def Show_Groups_List(self):

        driver = self.app.driver

        if driver.current_url.endswith("/group.php") and len (  driver.find_elements(By.NAME, "new") ) >0:
            return

        driver.find_element(By.LINK_TEXT, "groups").click()


    def Delete_First_Group (self):

        self.Delete_Group_By_Index(0)


        # Старая реализация до создания метода Delete_Group_By_Index
        # driver = self.app.driver
        #
        # self.Show_Groups_List()
        # time.sleep(1)
        #
        # self.Select_First_Group()
        #
        # # Нажать на кнопку Delete
        # driver.find_element(By.NAME, "delete").click()
        # time.sleep(1)
        #
        # self.Show_Groups_List()
        # time.sleep(1)
        #
        # self.group_cash = None # Кэш не валиден после добавлени, модификации, удаления групп


    def Edit_First_Group(self):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(1)

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

        time.sleep(1)

        # Нажать на кнопку Update
        driver.find_element(By.NAME, "update").click()

        time.sleep(1)

        # Открыть список групп

        self.Show_Groups_List()
        time.sleep(1)

        self.group_cash = None # Кэш не валиден после добавлени, модификации, удаления групп


    def Modify_First_Group(self, new_group_data):

        self.Modify_Group_By_Index(0, new_group_data)

        # Старая реализация до создяния метода:  Modify_Group_By_Index
        # driver = self.app.driver
        #
        # self.Show_Groups_List()
        # time.sleep(1)
        #
        # self.Select_First_Group()
        #
        # # Open modification form
        # driver.find_element(By.NAME, "edit").click()
        #
        # # Fill the form
        # self.Fill_Group_Form(new_group_data)
        #
        # # Submit midification
        # driver.find_element(By.NAME, "update").click()
        #
        # # Вернуться к списку групп
        # self.Show_Groups_List()
        # time.sleep(1)
        #
        # self.group_cash = None # Кэш не валиден после добавлени, модификации, удаления групп

    def Modify_Group_By_Index(self, index, new_group_data):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(1)

        self.Select_Group_By_Index(index)

        # Open modification form
        driver.find_element(By.NAME, "edit").click()

        # Fill the form
        self.Fill_Group_Form(new_group_data)

        # Submit midification
        driver.find_element(By.NAME, "update").click()

        # Вернуться к списку групп
        self.Show_Groups_List()
        time.sleep(1)

        self.group_cash = None # Кэш не валиден после добавлени, модификации, удаления групп




    def Select_First_Group(self):

        driver = self.app.driver

        self.Show_Groups_List()

        # Выбрать первый по списку чек-бокс

        driver.find_element(By.NAME, "selected[]").click()

    def Select_Group_By_Index(self, index):

        driver = self.app.driver

        self.Show_Groups_List()

        # Выбрать первый по списку чек-бокс

        driver.find_elements(By.NAME, "selected[]")[index].click()


    def count(self):

        driver = self.app.driver

        self.Show_Groups_List()

        count =  len( driver.find_elements(By.NAME, "selected[]") )

        return count

    group_cash = None

    def get_group_list(self):

        print ("Enter get_group_list: ")
        if self.group_cash is None:

            driver = self.app.driver

            self.Show_Groups_List()

            self.group_cash = []

            for element in driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                item = element.find_element(By.NAME, "selected[]")
                id = item.get_attribute("value")
                self.group_cash.append(Group(group_name=text,group_id=id))


        print (self.group_cash)

        print ("Exit get_group_list: ")

        return list(self.group_cash)



    def Delete_Group_By_Index (self, index):

        driver = self.app.driver

        self.Show_Groups_List()
        time.sleep(1)

        self.Select_Group_By_Index(index)

        # Нажать на кнопку Delete
        driver.find_element(By.NAME, "delete").click()
        time.sleep(1)

        self.Show_Groups_List()
        time.sleep(1)

        self.group_cash = None # Кэш не валиден после добавлени, модификации, удаления групп









