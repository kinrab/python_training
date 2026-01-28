
from MODEL.contact import Contact

#######################################################################################################################
# Вариант параметризации через фикстуру: Динамическое связывание в функции def pytest_generate_tests(metafunc):
# И загрузку из файла DATA/contact.json сгенерированного генератором: generator\gen_contact.py
#######################################################################################################################
def test_add_new_contact_version_second(app, json_contacts):

    usercontact = json_contacts
    old_contact_list = app.contact.get_contact_list()
    app.contact.Add_new_contact(usercontact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == app.contact.count() # В новом списке должно быть на один контакт больше

    txt_fname =  "Select (" + usercontact.first_name +" " + usercontact.last_name + ")"
    usercontact.first_name = txt_fname
    old_contact_list.append(usercontact)

    assert sorted(old_contact_list, key = Contact.id_or_max) == sorted(new_contact_list, key = Contact.id_or_max)

#######################################################################################################################
# Вариант параметризации через фикстуру: Динамическое связывание в функции def pytest_generate_tests(metafunc):
#######################################################################################################################
def test_add_new_contact_version_first(app, data_contacts):

    usercontact = data_contacts
    old_contact_list = app.contact.get_contact_list()
    app.contact.Add_new_contact(usercontact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == app.contact.count() # В новом списке должно быть на один контакт больше

    txt_fname =  "Select (" + usercontact.first_name +" " + usercontact.last_name + ")"
    usercontact.first_name = txt_fname
    old_contact_list.append(usercontact)

    assert sorted(old_contact_list, key = Contact.id_or_max) == sorted(new_contact_list, key = Contact.id_or_max)


#######################################################################################################################
# Вариант через параметризацию @pytest.mark.parametrize
#######################################################################################################################
from DATA.contacts import constant as test_data
import pytest

@pytest.mark.parametrize("user_contact", test_data, ids =[repr(x) for x in test_data ] )

def test_add_new_contact(app, user_contact):

    usercontact = user_contact

    old_contact_list = app.contact.get_contact_list()

    # user_contact =  Contact( first_name = "Иванов",
    #                                      middle_name = "Иван",
    #                                      last_name = "Иванович",
    #                                      nick_name= "Ванька",
    #                                      contact_title =  "ИИИ",
    #                                      company_name= "ООО_Рога_и_Копыта",                        # Если вводить с пробелами то SQL запрос внутри приложения дает ошибку и не сохраняет данные (всегда или иногда!)
    #                                      contact_address = "Проспект Ленина, дом 15, кв 7",
    #                                      home_phone =  "+7 821 000-00-00",
    #                                      mobile_phone = "+7 921 000-00-00",
    #                                      work_phone = "+7 812 000-00-01",
    #                                      fax_phone = "+7 812 000-00-02",
    #                                      contact_email1= "iii1@mail.ru",
    #                                      contact_email2 = "iii2@mail.ru",
    #                                      contact_email3 = "iii3@mail.ru",
    #                                      home_page = "http://www.leningrad.spb.ru",
    #                                      birthday_day = 1 ,
    #                                      birthday_month = 'January',
    #                                      birthday_year = "1980",
    #                                      anniversary_day =  1,
    #                                      anniversary_month = 'January',
    #                                      anniversary_year = 1980,
    #                                      second_address = "Улица Советская, дом 18, кв 8",
    #                                      second_home = "http://www.leningrad.spb.ru",
    #                                      second_notes = "Просто какой-то комментарий" )

    app.contact.Add_new_contact(usercontact)

    new_contact_list = app.contact.get_contact_list()

    assert len(old_contact_list) + 1 == app.contact.count() # В новом списке должно быть на один контакт больше

    txt_fname =  "Select (" + usercontact.first_name +" " + usercontact.last_name + ")"

    usercontact.first_name = txt_fname

    old_contact_list.append(usercontact)

    #assert old_sorted_list == new_sorted_list

    assert sorted(old_contact_list, key = Contact.id_or_max) == sorted(new_contact_list, key = Contact.id_or_max)

    # app.session.Logout_process()
    # time.sleep(3)