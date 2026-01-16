
import pytest
import time

from FIXTURE.application import Application

fixture = None

@pytest.fixture

def app(request):

    global fixture

    if fixture is None:
        fixture = Application()
    else:
        if  not fixture.is_valid():
            fixture = Application()

    print("Start fixture login:\n")

    fixture.session.Ensure_Login_process(username = "admin", password = "secret")

    print("End fixture login.\n")

    return fixture


@pytest.fixture( scope="session", autouse = True )

def stop(request):
    def fin():
         fixture.session.Ensure_Logout_process()
         fixture.Destroy()

    request.addfinalizer(fin)
    return fixture

