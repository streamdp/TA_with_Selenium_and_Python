import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: ru, en, ... (etc.)')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    print('user_language:', user_language)
    if browser_name == "chrome":
        if user_language != 'none':
            print("\nstart chrome browser for test..")
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
            browser = webdriver.Chrome(options=options)
        else:
            raise pytest.UsageError("--language should be set (ru / en / etc..)")
    elif browser_name == "firefox":
        if user_language != 'none':
            fp = webdriver.FirefoxProfile()
            fp.set_preference('intl.accept_languages', user_language)
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--language should be set (ru / en / etc..)")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
