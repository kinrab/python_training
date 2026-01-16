from MODEL.group import Group
import time

def test_del_first_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    if app.group.count() == 0:

          app.group.Add_New_Group( Group( group_name = "TestGroup #0", group_header = "test_group_0_header", group_footer = "test_group_0_footer") )

    app.group.Delete_First_Group()
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)