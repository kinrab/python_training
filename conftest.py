
import pytest
import time

from FIXTURE.application import Application

fixture = None

@pytest.fixture

def app(request):

    global fixture

    select_browser = request.config.getoption("--browser")
    base_URL = request.config.getoption("--baseURL")

    if (fixture is None) or not fixture.is_valid():
        fixture = Application(browser = select_browser, base_url = base_URL)

    fixture.session.Ensure_Login_process(username = "admin", password = "secret")

    return fixture


@pytest.fixture( scope="session", autouse = True )

def stop(request):
    def fin():
         fixture.session.Ensure_Logout_process()
         fixture.Destroy()

    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox" )
    parser.addoption("--baseURL", action="store", default="http://localhost:8080/addressbook/" )