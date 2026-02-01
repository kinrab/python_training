from MODEL.group import Group
from random import randrange
import random

import time

# Удалить случайно выбранную группу - вариант с DB get_group_list
def test_del_some_group_db(app, db, check_ui):

    if len(db.get_group_list()) == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #0", group_header = "test_group_0_header", group_footer = "test_group_0_footer") )

    old_group_list = db.get_group_list()

    group = random.choice(old_group_list)

    app.group.Delete_Group_By_id(group.group_id)
    time.sleep(3)

    new_group_list =  db.get_group_list()

    assert len(old_group_list)-1 == len(new_group_list) # Проверка избыточна так как есть ниже

    #old_group_list [index:index+1] = []   # Удаляем элемент с индексом index из списка
    old_group_list.remove(group)

    assert old_group_list == new_group_list

    if check_ui: # Проверку будем выполнять только если флаг установлен
        assert sorted(new_group_list, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)


# Удалить случайно выбранную группу
def test_del_some_group(app):

    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #0", group_header = "test_group_0_header", group_footer = "test_group_0_footer") )

    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))

    app.group.Delete_Group_By_Index(index)
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    assert len(old_group_list)-1 == len(new_group_list) # Проверка избыточна так как есть ниже

    old_group_list [index:index+1] = []   # Удаляем элемент с индексом index из списка

    assert old_group_list == new_group_list



def test_del_first_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #0", group_header = "test_group_0_header", group_footer = "test_group_0_footer") )

    old_group_list = app.group.get_group_list()

    app.group.Delete_First_Group()
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    assert len(old_group_list)-1 == len(new_group_list) # Проверка избыточна так как есть ниже

    old_group_list [0:1] = []   # Удаляем первый элемент с индексом 0 из списка

    # DEBUG:

    # for element in old_group_list:
    #     print ("old list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")
    #
    # for element in new_group_list:
    #     print ("new list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")

    # END DEBUG

    assert old_group_list == new_group_list

    # app.session.Logout_process()
    # time.sleep(3)

