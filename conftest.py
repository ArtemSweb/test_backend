import pytest
import os.path
from fixture.application import Application

@pytest.fixture(scope='session')
def app():
    fixture = Application()
    return fixture