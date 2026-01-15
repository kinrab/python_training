# -*- coding: utf-8 -*-
import time

import pytest
from FIXTURE.application import Application
from MODEL.contact import Contact
from MODEL.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Destroy)
    return fixture

def test_add_new_contact(app):

    # Устанавливаем размеры окна приложения - надо ли оно?
    #self.driver.set_window_size(1920, 1200)

    # Открываем окно приложения: внутри метода логина
    # Логинимся с параметрами Login = admin Password = secret

    app.session.Login_process( username = "admin", password = "secret")

    time.sleep(3)

    user_contact =  Contact( first_name = "Иванов",
                                         middle_name = "Иван",
                                         last_name = "Иванович",
                                         nick_name= "Ванька",
                                         contact_title =  "ИИИ",
                                         company_name= "ООО_Рога_и_Копыта",                        # Если вводить с пробелами то SQL запрос внутри приложения дает ошибку и не сохраняет данные (всегда или иногда!)
                                         contact_address = "Проспект Ленина, дом 15, кв 7",
                                         home_phone =  "+7 821 000-00-00",
                                         mobile_phone = "+7 921 000-00-00",
                                         work_phone = "+7 812 000-00-01",
                                         fax_phone = "+7 812 000-00-02",
                                         contact_email1= "iii1@mail.ru",
                                         contact_email2 = "iii2@mail.ru",
                                         contact_email3 = "iii3@mail.ru",
                                         home_page = "http://www.leningrad.spb.ru",
                                         birthday_day = 1 ,
                                         birthday_month = 'January',
                                         birthday_year = "1980",
                                         anniversary_day =  1,
                                         anniversary_month = 'January',
                                         anniversary_year = 1980,
                                         second_address = "Улица Советская, дом 18, кв 8",
                                         second_home = "http://www.leningrad.spb.ru",
                                         second_notes = "Просто какой-то комментарий" )

    app.contact.Add_new_contact(user_contact)

    app.session.Logout_process()

    time.sleep(3)


def test_add_new_group(app):

    app.session.Login_process(username = "admin", password = "secret")
    time.sleep(3)

    app.group.Add_New_Group(Group( group_name = "Test_group", group_header = "test_group_header", group_footer = "test_group_footer"))
    time.sleep(3)

    app.session.Logout_process()
    time.sleep(3)

def test_add_new_empty_group(app):

    app.session.Login_process(username = "admin", password = "secret")
    time.sleep(3)

    app.group.Add_New_Group(Group( group_name = "", group_header = "", group_footer = ""))
    time.sleep(3)

    app.session.Logout_process()
    time.sleep(3)

