import pytest
from _pytest.fixtures import SubRequest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def driver(request:SubRequest):
    if request.config.getoption('--browser').upper() == 'FF':
        driver = webdriver.Firefox()
    elif request.config.getoption('--browser').lower() == 'chrome':
        driver = webdriver.Chrome()
    elif request.config.getoption('--browser').lower() == 'edge':
        driver = webdriver.Edge()
    yield driver
    driver.quit()
