
import time

def test_edit_first_group(app):

    # app.session.Login_process(username = "admin", password = "secret")
    # time.sleep(3)

    app.contact.Edit_First_Contact()
    time.sleep(3)

    # app.session.Logout_process()
    # time.sleep(3)