
from MODEL.group import Group
import random
import string

constant = [
            Group(group_name = "name1", group_header = "header1", group_footer = "footer1"),
            Group(group_name = "name2", group_header = "header2", group_footer = "footer2")
]

def random_string (prefix, maxlen):

    symbols_list =  string.ascii_letters + string.digits #  + " "*10      Убираем пробелы! Есть ошибка иначе

    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

# Вариант 1:
test_data_new = [Group(group_name = "", group_header = "", group_footer = "")] +  \
                  [Group(group_name = random_string("name", 10), group_header = random_string("header", 20), group_footer = random_string("footer", 20)) for i in range(3)]

# Вариант 2: с перебором комбинаторным
# test_data = [
#                    Group(group_name = name, group_header = footer, group_footer = header)
#                    for name in ["", random_string("name",10)]
#                    for header in ["", random_string("header",20)]
#                    for footer in ["", random_string("footer",20)]
# ]

