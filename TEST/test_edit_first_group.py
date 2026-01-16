import time


def test_edit_first_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    app.group.Edit_First_Group()
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)