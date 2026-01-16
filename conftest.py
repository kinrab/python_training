
import pytest
import time

from FIXTURE.application import Application

fixture = None

@pytest.fixture

def app(request):

    global fixture

    if fixture is None:
        fixture = Application()
        fixture.session.Login_process(username = "admin", password = "secret")
    else:
           if  not fixture.is_valid():
               fixture = Application()
               fixture.session.Login_process(username = "admin", password = "secret")
    return fixture


@pytest.fixture( scope="session", autouse = True )

def stop(request):
    def fin():
         time.sleep(3)
         fixture.session.Logout_process()
         time.sleep(3)
         fixture.Destroy()

    request.addfinalizer(fin)
    return fixture

