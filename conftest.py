
import pytest
from FIXTURE.application import Application


@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.Destroy)
    return fixture
