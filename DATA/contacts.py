from MODEL.contact import Contact
import random
import string

# Вариант 1 с константой:
constant = [
            Contact( first_name = "FirstName#1", middle_name = "MiddleName#1",last_name = "LastName#1",nick_name = "NickName#1",contact_title = "FMLN#1",
                     company_name = "CompanyName#1", contact_address = "Address#1", home_phone = "+7(812)000-00-00", mobile_phone = "+7(921)000-00-00",
                     work_phone = "+7(812)777-77-77", fax_phone = "+7(812)888-88-88", contact_email1 = "contact1@mail.ru",
                     contact_email2 = "contact1@mail2.ru", contact_email3 = "contact1@mail3.ru", home_page = "www.leningrad.spb.ru",
                     birthday_day = 1, birthday_month = "January", birthday_year = "1980", anniversary_day = 1, anniversary_month = "January", anniversary_year = "1980",
                     second_address = "Address 2 for contact 1",second_home = "piter.spb.ru", second_notes = "Notes contact1", contact_id = None ),
            Contact( first_name = "FirstName#2", middle_name = "MiddleName#2",last_name = "LastName#2",nick_name = "NickName#2",contact_title = "FMLN#2",
                     company_name = "CompanyName#2", contact_address = "Address#2", home_phone = "+7(812)000-00-02", mobile_phone = "+7(921)000-00-02",
                     work_phone = "+7(812)777-77-72", fax_phone = "+7(812)888-88-82", contact_email1 = "contact2@mail.ru",
                     contact_email2 = "contact2@mail2.ru", contact_email3 = "contact2@mail3.ru", home_page = "www2.leningrad.spb.ru",
                     birthday_day = 11, birthday_month = "January", birthday_year = "1985", anniversary_day = 11, anniversary_month = "January", anniversary_year = "1985",
                     second_address = "Address 2 for contact 1",second_home = "2piter.spb.ru", second_notes = "Notes contact2", contact_id = None ),
]

def random_string (prefix, maxlen):
    symbols_list =  string.ascii_letters + string.digits #  + " "*10      Убираем пробелы! Есть ошибка иначе
    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

def random_digit_string (prefix, maxlen):
    symbols_list =   string.digits
    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

# Вариант 2 с генерацией n контактов:

test_data_new = [ Contact(first_name = random_string("first_name"+ str(i), 10),
                         middle_name = random_string("middle_name", 10),
                         last_name = random_string("last_name", 10),
                         nick_name = random_string("nick_name", 10),
                         contact_title = random_string("contact_title", 10),
                         company_name = random_string("company_name", 10),
                         contact_address =  random_string("company_name", 20),
                         home_phone = random_digit_string("+7(812)", 7),
                         mobile_phone =  random_digit_string("+7(921)", 7),
                         work_phone = random_digit_string("+7(813)", 7),
                         fax_phone = random_digit_string("+7(814)", 7),
                         contact_email1 =  random_string("contact_", 5)+"@mail.ru",
                         contact_email2 = random_string("contact_", 5)+"@yandex.ru",
                         contact_email3 = random_string("contact_", 5)+"@inbox.ru",
                         home_page = random_string("https://", 10),
                         birthday_day = random.randint(1, 31),
                         birthday_month = "January",
                         birthday_year = random.randint(1970, 2000),
                         anniversary_day = random.randint(1, 31),
                         anniversary_month = "January",
                         anniversary_year = random.randint(1970, 2000),
                         second_address = random_string("second_address", 15),
                         second_home = random_string("second_home", 15),
                         second_notes = random_string("second_notes", 20),
                         contact_id = None ) for i in range(3)
]

