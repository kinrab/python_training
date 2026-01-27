import importlib

from FIXTURE.application import Application
import importlib
import os.path
import pytest
import jsonpickle
import json


fixture = None
parameters = None

@pytest.fixture

def app(request):

    global fixture
    global parameters

    select_browser = request.config.getoption("--browser")

    if parameters is None:

        cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--config"))

        with open(cfg_file) as config_file:
            parameters = json.load(config_file)

    if (fixture is None) or not fixture.is_valid():
        fixture = Application(browser = select_browser, base_url = parameters['baseUrl'])

    fixture.session.Ensure_Login_process(username = parameters['username'], password = parameters['password'])

    return fixture


@pytest.fixture( scope="session", autouse = True )

def stop(request):
    def fin():
         fixture.session.Ensure_Logout_process()
         fixture.Destroy()

    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json" )
    parser.addoption("--browser", action="store", default="firefox" )

def pytest_generate_tests(metafunc):

    for fixture in metafunc.fixturenames:

        if fixture.startswith("data_"):
            testdatalocA = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdatalocA, ids=[str(x) for x in testdatalocA])
        elif fixture.startswith("json_"):
            testdatalocB = load_from_json_file(fixture[5:])
            metafunc.parametrize(fixture,testdatalocB, ids=[str(x) for x in testdatalocB])

def load_from_module (module):
    str_name = "DATA.%s" % module
    x = importlib.import_module(str_name).test_data_new # x = importlib.import_module(str_name).constant   # Или можно взять constant из файла DATA\groups.py
    return x

def load_from_json_file (file):
    with open( os.path.join(os.path.dirname(os.path.abspath(__file__)),"DATA/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
