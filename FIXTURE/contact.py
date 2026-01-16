from selenium.webdriver.common.by import By
import time

class ContactHelper:

    def __init__(self,app):

        self.app = app

    def Add_new_contact(self, new_contact):

        driver = self.app.driver

        # Кликаем по меню - создать новый контакт
        driver.find_element(By.LINK_TEXT, "add new").click()
        #print("STEP 1 - START TEST\n")

        # Заполняем поле firstname
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(new_contact.first_name)
        #print("STEP 2\n")

        # Заполняем middle_name
        driver.find_element(By.NAME, "middlename").click()
        driver.find_element(By.NAME, "middlename").clear()
        driver.find_element(By.NAME, "middlename").send_keys(new_contact.middle_name)
        #print("STEP 3\n")

        # Заполняем поле last_name
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").clear()
        driver.find_element(By.NAME, "lastname").send_keys(new_contact.last_name)
        #print("STEP 4\n")

        driver.find_element(By.NAME, "nickname").click()
        driver.find_element(By.NAME, "nickname").clear()
        driver.find_element(By.NAME, "nickname").send_keys(new_contact.nick_name)
        #print("STEP 5\n")

        # Добавление картинки пока пропустим
        # self.driver.find_element(By.NAME, "photo").click()
        # self.driver.find_element(By.NAME, "photo").send_keys("C:\\fakepath\\Avatar.png")

        # Добавление поля tittle
        driver.find_element(By.NAME, "title").click()
        driver.find_element(By.NAME, "title").clear()
        driver.find_element(By.NAME, "title").send_keys(new_contact.contact_title)
        #print("STEP 6\n")

        # Добавление имени компании:
        driver.find_element(By.NAME, "company").click()
        driver.find_element(By.NAME, "company").clear()
        driver.find_element(By.NAME, "company").send_keys(new_contact.company_name)
        #print("STEP 7\n")

        # Добавление адреса:
        driver.find_element(By.NAME, "address").click()
        driver.find_element(By.NAME, "address").clear()
        driver.find_element(By.NAME, "address").send_keys(new_contact.contact_address)
        #print("STEP 8\n")

       # Добавление домашнего ТЕЛЕФОНА:
        driver.find_element(By.NAME, "home").click()
        driver.find_element(By.NAME, "home").clear()
        driver.find_element(By.NAME, "home").send_keys(new_contact.home_phone)
        #print("STEP 9\n")

        # Добавление МОБИЛЬНОГО ТЕЛЕФОНА:
        driver.find_element(By.NAME, "mobile").click()
        driver.find_element(By.NAME, "mobile").clear()
        driver.find_element(By.NAME, "mobile").send_keys(new_contact.mobile_phone)
        #print("STEP 10\n")

        # Добавление РАБОЧЕГО ТЕЛЕФОНА:
        driver.find_element(By.NAME, "work").click()
        driver.find_element(By.NAME, "work").send_keys(new_contact.work_phone)
        #print("STEP 11\n")

        # Добавление НОМЕРА ФАКСА:
        driver.find_element(By.NAME, "fax").click()
        driver.find_element(By.NAME, "fax").clear()
        driver.find_element(By.NAME, "fax").send_keys(new_contact.fax_phone)
        #print("STEP 12\n")

        # Добавление первого email:
        driver.find_element(By.NAME, "email").click()
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "email").send_keys(new_contact.contact_email1)
        #print("STEP 13\n")

        # Добавление второго email:
        driver.find_element(By.NAME, "email2").click()
        driver.find_element(By.NAME, "email2").clear()
        driver.find_element(By.NAME, "email2").send_keys(new_contact.contact_email2)
        #print("STEP 14\n")

        # Добавление третьего email:
        driver.find_element(By.NAME, "email3").click()
        driver.find_element(By.NAME, "email3").clear()
        driver.find_element(By.NAME, "email3").send_keys(new_contact.contact_email3)
        #print("STEP 15\n")

        # Добавляем поле Home Page:
        driver.find_element(By.NAME, "homepage").click()
        driver.find_element(By.NAME, "homepage").clear()
        driver.find_element(By.NAME, "homepage").send_keys(new_contact.home_page)
        #print("STEP 16\n")

        # Выбираем в выпадающем списке число 1:
        driver.find_element(By.NAME, "bday").click()
        dropdown = driver.find_element(By.NAME, "bday")
        str_element =  "//option[. = '" + str(new_contact.birthday_day) + "']"

        # Строка должна быть такая:  "//option[. = '1']"    чтобы полная команда была бы: dropdown.find_element(By.XPATH, "//option[. = '1']").click()
        #print ("Сформировали строку: " + str_element)

        dropdown.find_element(By.XPATH, str_element).click()
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(61) > option:nth-child(3)").click()

        #print("STEP 17\n")

        # Выбираем в выпадающем списке месяц
        driver.find_element(By.NAME, "bmonth").click()
        dropdown = driver.find_element(By.NAME, "bmonth")

        str_element =  "//option[. = '" + new_contact.birthday_month + "']"
        #print ("Сформировали строку: " + str_element)

        dropdown.find_element(By.XPATH, str_element).click()
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(62) > option:nth-child(2)").click()

        #dropdown.find_element(By.XPATH, "//option[. = 'January']").click()
        #print("STEP 18\n")

        # Вводим год рождния в соответствующее поле:
        driver.find_element(By.NAME, "byear").click()
        driver.find_element(By.NAME, "byear").send_keys(new_contact.birthday_year)
        #print("STEP 19\n")

        # Вводим дату празднования дня рожденья:
        driver.find_element(By.NAME, "aday").click()
        dropdown = driver.find_element(By.NAME, "aday")
        str_element =  "//option[. = '" + str(new_contact.birthday_day) + "']"

        # Строка должна быть такая:  "//option[. = '1']"    чтобы полная команда была бы: dropdown.find_element(By.XPATH, "//option[. = '1']").click()
        #print ("Сформировали строку: " + str_element)

        dropdown.find_element(By.XPATH, str_element).click()
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(66) > option:nth-child(3)").click()

        #print("STEP 20\n")

        # Выбираем в выпадающем списке месяц празднования ДР:
        driver.find_element(By.NAME, "amonth").click()
        dropdown = driver.find_element(By.NAME, "amonth")

        str_element =   "//option[. = '"+ new_contact.anniversary_month + "']"
        #print ("Сформировали строку: " + str_element)

        dropdown.find_element(By.XPATH, str_element ).click()
        driver.find_element(By.CSS_SELECTOR, "select:nth-child(67) > option:nth-child(2)").click()
        #dropdown.find_element(By.XPATH, "//option[. = 'January']").click()
        #print("STEP 21\n")

        # Водим год празднования ДР:
        driver.find_element(By.NAME, "ayear").click()
        driver.find_element(By.NAME, "ayear").send_keys(new_contact.anniversary_year)
        #print("STEP 22\n")

        # Вводим второй адрес:
        driver.find_element(By.NAME, "address2").click()
        driver.find_element(By.NAME, "address2").send_keys(new_contact.second_address)
        #print("STEP 23\n")

        # Вводим второй  Home - это видимо второй домашний телефон?
        driver.find_element(By.NAME, "phone2").click()
        driver.find_element(By.NAME, "phone2").send_keys(new_contact.second_home)
        #print("STEP 24\n")

        # Вводим примечание в разделе Secondary:
        driver.find_element(By.NAME, "notes").click()
        driver.find_element(By.NAME, "notes").send_keys(new_contact.second_notes)
        #print("STEP 25\n")

        time.sleep(3)

        # Нажимаем на кнопу "Enter":
        #driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()            # исходный код клика по кнопке Enter полученный рекордером Selenium IDE / Katalon
        driver.find_element(By.NAME, "submit").click()                                              # - вроде так проще и понятнее должно быть чем CSS selector?

        #print("STEP 26 - END OF TEST\n")
        #time.sleep(1)

    def Show_Contact_List(self):

        driver = self.app.driver

        # Нажать на кнопку Home что по факту откроет список контактов:
        driver.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
        time.sleep(3)

    def Delete_First_Contact(self):

        driver = self.app.driver

        # Открыть страницу контактов после окончания теста добавления пустой группы ! иначе тесты упадут !
        self.app.contact.Show_Contact_List()
        time.sleep(3)

        # Выбираем первый контакт в списке - Check box activate
        driver.find_element(By.NAME, "selected[]").click()

        # Нажимаем кнопку Delete
        driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(3)

        # Подтверждаем удаление во всплывающем окне

        assert driver.switch_to.alert.text == "Delete 1 addresses?"

        alert = driver.switch_to.alert

        alert.accept()

        time.sleep(3)  # Далее приложение автоматически откроет список оствашихся контактов

    def Edit_First_Contact(self):

        driver = self.app.driver

        # Открыть страницу контактов после окончания теста добавления пустой группы ! иначе тесты упадут !
        self.app.contact.Show_Contact_List()
        time.sleep(3)

        # Нажимаем кнопку Edit у первого контакта  xpath = //img[@alt='Edit']
        driver.find_element(By.XPATH, "//img[@alt='Edit']").click()
        time.sleep(3)

        # Изменяем firstname поле новым значением
        item = driver.find_element(By.NAME, "firstname")
        val = item.get_attribute("value")

        print(" Исходное значение: {  "+ val + " }")

        val = val + "(*)"

        print("Новое значение: {  "+ val + " }")

        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").clear()
        driver.find_element(By.NAME, "firstname").send_keys(val)

        time.sleep(3)

        # Жмем кнопку Update
        driver.find_element(By.XPATH, "//input[@value='Update']").click()
        time.sleep(3)

        # Через 2 секунды автоматически открывается страница контактов



