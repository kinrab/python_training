
from MODEL.group import Group
from random import randrange
import time


def test_modify_group_name_of_some_group(app):

    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #S", group_header = "test_group_S_header", group_footer = "test_group_S_footer") )

    old_group_list = app.group.get_group_list()

    index = randrange(len(old_group_list)) # Выбрать случайную группу

    group = Group(group_name = "Test group A modify")
    group.group_id = old_group_list[index].group_id

    app.group.Modify_Group_By_Index(index, group)
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    assert len(old_group_list)  == len(new_group_list)

    old_group_list[index] = group

    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)





def test_modify_group_name_of_first_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #S", group_header = "test_group_S_header", group_footer = "test_group_S_footer") )

    old_group_list = app.group.get_group_list()

    group = Group(group_name = "Group name A")
    group.group_id = old_group_list[0].group_id

    app.group.Modify_First_Group(group)
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    assert len(old_group_list)  == len(new_group_list)

    old_group_list[0] = group

    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)


    # app.session.Logout_process()
    # time.sleep(3)


def test_modify_group_header_of_first_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #M", group_header = "test_group_M_header", group_footer = "test_group_M_footer") )

    old_group_list = app.group.get_group_list()

    # DEBUG:
    # for element in old_group_list:
    #     print("old list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")
    # END DEBUG

    group = Group(group_header = "Group name B")
    group.group_id = old_group_list[0].group_id
    group.group_name = old_group_list[0].group_name

    app.group.Modify_First_Group(group)
    time.sleep(3)

    new_group_list =  app.group.get_group_list()

    # for element in new_group_list:
    #     print("new list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")

    assert len(old_group_list) == len(new_group_list)

    old_group_list[0] = group

    # for element in old_group_list:
    #     print("old list item: name=" + element.group_name + " id = " + str(element.group_id) + "\n")

    assert sorted(old_group_list, key = Group.id_or_max) == sorted(new_group_list, key = Group.id_or_max)

    # app.session.Logout_process()
    # time.sleep(3)



