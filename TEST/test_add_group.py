# -*- coding: utf-8 -*-
from MODEL.group import Group
import time


def test_add_new_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    old_group_list = app.group.get_group_list()

    group =  Group(group_name = "Test_group", group_header = "test_group_header", group_footer = "test_group_footer")

    app.group.Add_New_Group(group)
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    assert len(old_group_list) + 1 == app.group.count()

    new_group_list =  app.group.get_group_list()

    old_group_list.append(group)

    # # DEBUG:
    #
    # for element in old_group_list:
    #     print("old list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")
    #
    # for element in new_group_list:
    #     print("new list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")
    #
    # # END DEBUG

    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)

    # app.session.Logout_process()
    # time.sleep(3)


def test_add_new_empty_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    old_group_list = app.group.get_group_list()

    group =  Group(group_name = "", group_header = "", group_footer = "")

    app.group.Add_New_Group(Group( group_name = "", group_header = "", group_footer = ""))
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    assert len(old_group_list) + 1 == len(new_group_list)

    old_group_list.append(group)

    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)

    # app.session.Logout_process()
    # time.sleep(3)

