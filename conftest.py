import importlib

from FIXTURE.application import Application
import importlib
import os.path
import pytest
import jsonpickle
import json
from FIXTURE.db import DbFixture


AppFixture = None
parameters = None

def load_config(file):
    global parameters
    if parameters is None:
        cfg_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)

        with open(cfg_file) as config_file:
            parameters = json.load(config_file)
    return parameters

@pytest.fixture
def app(request):

    global AppFixture

    web_config = load_config(request.config.getoption("--config"))['web']

    if (AppFixture is None) or not AppFixture.is_valid():

        AppFixture = Application(browser =  web_config['browser'], base_url =  web_config['baseUrl'])

    AppFixture.session.Ensure_Login_process(username =  web_config['username'], password =  web_config['password'])

    return AppFixture

@pytest.fixture
def db(request):

    db_config = load_config(request.config.getoption("--config"))['db']

    dbFixture = DbFixture(host = db_config['host'],
                          name = db_config['name'],
                          user = db_config['user'],
                          password = db_config['password'])

    def fin():
        dbFixture.destroy()

    request.addfinalizer(fin)
    return dbFixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


@pytest.fixture( scope="session", autouse = True )
def stop(request):
    def fin():
         AppFixture.session.Ensure_Logout_process()
         AppFixture.Destroy()

    request.addfinalizer(fin)
    return AppFixture

def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json" )
    parser.addoption("--check_ui", action="store_true")
    #parser.addoption("--browser", action="store", default="firefox" ) # Перенесли в конфиг!

# metafunc в Python — это объект, используемый в фреймворке pytest внутри хук-функции pytest_generate_tests для динамической параметризации тестов.
# Он позволяет генерировать тестовые случаи «на лету», анализировать аргументы функций и создавать вариации тестов без использования
# декоратора @pytest.mark.parametrize для каждого случая.

def pytest_generate_tests(metafunc):

    for AppFixture in metafunc.fixturenames:

        if AppFixture.startswith("data_"):
            testdatalocA = load_from_module(AppFixture[5:])
            metafunc.parametrize(AppFixture, testdatalocA, ids=[str(x) for x in testdatalocA])
        elif AppFixture.startswith("json_"):
            testdatalocB = load_from_json_file(AppFixture[5:])
            metafunc.parametrize(AppFixture,testdatalocB, ids=[str(x) for x in testdatalocB])

def load_from_module (module):
    str_name = "DATA.%s" % module
    x = importlib.import_module(str_name).test_data_new # x = importlib.import_module(str_name).constant   # Или можно взять constant из файла DATA\groups.py
    return x

def load_from_json_file (file):
    with open( os.path.join(os.path.dirname(os.path.abspath(__file__)),"DATA/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())
