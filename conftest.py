
import pytest
import time

from FIXTURE.application import Application


@pytest.fixture (scope = "session")
def app(request):

    fixture = Application()
    fixture.session.Login_process(username = "admin", password = "secret")
    def fin():
         time.sleep(3)
         fixture.session.Logout_process()
         time.sleep(3)
         fixture.Destroy()

    request.addfinalizer(fin)
    return fixture

