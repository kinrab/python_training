
from MODEL.group import Group
import os.path
import random
import string
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups","file"] )
except getopt.GetoptError as Err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/groups.json"

for o , a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string (prefix, maxlen):

    symbols_list =  string.ascii_letters + string.digits #  + " "*10      Убираем пробелы! Есть ошибка иначе

    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

# Вариант 1:
test_data = [Group(group_name = "", group_header = "", group_footer = "")] +  \
                  [Group(group_name = random_string("name", 10), group_header = random_string("header", 20), group_footer = random_string("footer", 20)) for i in range(n)]

data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(data_file,"w") as data_f:
    jsonpickle.set_encoder_options("json", indent = 2)
    data_f.write( jsonpickle.encode(test_data))
