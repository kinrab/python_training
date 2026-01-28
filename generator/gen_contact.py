# Параметры для запуска: gen_contact.py -n 3 -f data/contact.json
#
#  n 3 - число контактов которые нужно сгенерировать генератору
#  f data/contact.json - имя файла и папка в которой он находится


from MODEL.contact import Contact
import os.path
import random
import string
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts","file"] )
except getopt.GetoptError as Err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o , a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string (prefix, maxlen):

    symbols_list =  string.ascii_letters + string.digits #  + " "*10      Убираем пробелы! Есть ошибка иначе

    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

def random_digit_string (prefix, maxlen):
    symbols_list =   string.digits
    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

# Вариант 1:
test_data = [Contact(first_name = random_string("first_name"+ str(i), 10),
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
                     contact_id = None ) for i in range(n)
             ]


data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(data_file,"w") as data_f:
    jsonpickle.set_encoder_options("json", indent = 2)
    data_f.write( jsonpickle.encode(test_data))