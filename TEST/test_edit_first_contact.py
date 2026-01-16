
from MODEL.contact import Contact
import time

def test_edit_first_contact(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    if app.contact.count() == 0:

        user_contact =  Contact( first_name = "Петров",
                                             middle_name = "Петр",
                                             last_name = "Петрович",
                                             nick_name= "Петька",
                                             contact_title =  "ППП",
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

    app.contact.Edit_First_Contact()
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)
