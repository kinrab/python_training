
from MODEL.group import Group
import time


def test_modify_group_name(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    app.group.Modify_First_Group(Group(group_name = "XXL group name"))
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)


def test_modify_group_header(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    app.group.Modify_First_Group(Group(group_header = "XXL group header"))
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)