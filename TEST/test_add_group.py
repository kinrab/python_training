# -*- coding: utf-8 -*-
from MODEL.group import Group
import pytest
import random
import string
import time

def random_string (prefix, maxlen):

    symbols_list =  string.ascii_letters + string.digits #  + " "*10      Убираем пробелы! Есть ошибка иначе

    return prefix + "".join( [ random.choice(symbols_list) for i in range( random.randrange(maxlen)) ] )

#Вариает 1:
test_data = [Group(group_name = "", group_header = "", group_footer = "")] +  \
                  [Group(group_name = random_string("name", 10), group_header = random_string("header", 20), group_footer = random_string("footer", 20)) for i in range(3)]

# Вариант 2: с перебором комбинаторным
# test_data = [
#                    Group(group_name = name, group_header = footer, group_footer = header)
#                    for name in ["", random_string("name",10)]
#                    for header in ["", random_string("header",20)]
#                    for footer in ["", random_string("footer",20)]
# ]


@pytest.mark.parametrize("group", test_data, ids =[repr(x) for x in test_data ] )

def test_add_new_group(app, group):

    error = False

    old_group_list = app.group.get_group_list()

    app.group.Add_New_Group(group)
    time.sleep(1)

    new_group_list =  app.group.get_group_list()

    dlina = app.group.count()

    assert len(old_group_list) + 1 == dlina

    new_group_list =  app.group.get_group_list()

    group.group_header = None
    group.group_footer = None
    old_group_list.append(group)

    old_sorted_list =  sorted(old_group_list, key = Group.id_or_max)

    new_sorted_list  = sorted(new_group_list, key = Group.id_or_max)

    assert old_sorted_list == new_sorted_list


    # for i in range( dlina ):
    #
    #     if  (old_sorted_list[i].group_name   != new_sorted_list[i].group_name)   or \
    #         (old_sorted_list[i].group_header != new_sorted_list[i].group_header) or\
    #         (old_sorted_list[i].group_footer  != new_sorted_list[i].group_footer)  or\
    #         (old_sorted_list[i].group_id        != new_sorted_list[i].group_id):
    #         print("_________________")
    #         print("Comparation Error:  index:" + str(i))
    #         print (old_sorted_list[i])
    #         print (new_sorted_list[i])
    #         error = True
    #
    # assert error


    #assert old_sorted_list == new_sorted_list
    #assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)








# Устарело после добавления параметров со списком групп для тестов:
# def test_add_new_empty_group(app):
#
#     # app.session.Login_process(username = "admin", password = "secret")
#     # time.sleep(3)
#
#     old_group_list = app.group.get_group_list()
#
#     group =  Group(group_name = "", group_header = "", group_footer = "")
#
#     app.group.Add_New_Group(Group( group_name = "", group_header = "", group_footer = ""))
#     time.sleep(3)
#
#     new_group_list =  app.group.get_group_list()
#
#     assert len(old_group_list) + 1 == len(new_group_list)
#
#     old_group_list.append(group)
#
#     assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)
#
#     # app.session.Logout_process()
#     # time.sleep(1)

