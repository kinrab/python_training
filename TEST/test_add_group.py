# -*- coding: utf-8 -*-

from MODEL.group import Group
import time

###########################################################################################################################
# Вариант параметризации через фикстуру c загрузкой из файла формата JSON
###########################################################################################################################
def test_add_new_group_version_third(app, json_groups):

    group = json_groups

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


###########################################################################################################################
# Вариант параметризации через фикстуру:  Динамическое связываение
###########################################################################################################################

# def test_add_new_group_version_second(app, data_groups):
#
#     group = data_groups
#
#     old_group_list = app.group.get_group_list()
#
#     app.group.Add_New_Group(group)
#     time.sleep(1)
#
#     new_group_list =  app.group.get_group_list()
#
#     dlina = app.group.count()
#
#     assert len(old_group_list) + 1 == dlina
#
#     new_group_list =  app.group.get_group_list()
#
#     group.group_header = None
#     group.group_footer = None
#     old_group_list.append(group)
#
#     old_sorted_list =  sorted(old_group_list, key = Group.id_or_max)
#
#     new_sorted_list  = sorted(new_group_list, key = Group.id_or_max)
#
#     assert old_sorted_list == new_sorted_list



###########################################################################################################################
# Вариант параметризации через Pytest Mark Parameters:
###########################################################################################################################
#from DATA.groups import constant as test_data
#import pytest

# @pytest.mark.parametrize("group", test_data, ids =[repr(x) for x in test_data ] )
#
# def test_add_new_group_version_first(app, group):
#
#     #error = False
#
#     old_group_list = app.group.get_group_list()
#
#     app.group.Add_New_Group(group)
#     time.sleep(1)
#
#     new_group_list =  app.group.get_group_list()
#
#     dlina = app.group.count()
#
#     assert len(old_group_list) + 1 == dlina
#
#     new_group_list =  app.group.get_group_list()
#
#     group.group_header = None
#     group.group_footer = None
#     old_group_list.append(group)
#
#     old_sorted_list =  sorted(old_group_list, key = Group.id_or_max)
#
#     new_sorted_list  = sorted(new_group_list, key = Group.id_or_max)
#
#     assert old_sorted_list == new_sorted_list


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






