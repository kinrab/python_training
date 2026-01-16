
from MODEL.group import Group
import time


def test_modify_group_name(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)
    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #S", group_header = "test_group_S_header", group_footer = "test_group_S_footer") )

    app.group.Modify_First_Group(Group(group_name = "UPD group name"))
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)


def test_modify_group_header(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    if app.group.count() == 0:

        app.group.Add_New_Group( Group( group_name = "TestGroup #M", group_header = "test_group_M_header", group_footer = "test_group_M_footer") )

    app.group.Modify_First_Group(Group(group_header = "MOD group header"))
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)