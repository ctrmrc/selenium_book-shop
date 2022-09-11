from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--lang', action='store', default='en-gb',
                     help='Please choose language from this list: en-gb, ru')
    parser.addoption('--br', action='store', default='chrome',
                     help='Please choose browser from this list: chrome, firefox')

@pytest.fixture(scope='function')
def driver(request):
    chooseLang = request.config.getoption('lang')
    chooseBrowser = request.config.getoption('br')
    if chooseBrowser == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    print('\n!---TEST START---!')
    url = f'http://selenium1py.pythonanywhere.com/{chooseLang}/'
    driver.get(url)
    yield driver
    print('\n!---TEST FINISH---!')
    driver.quit()


