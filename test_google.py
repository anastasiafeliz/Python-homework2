import pytest
from browser import browser


@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)

    @pytest.fixture()
    def open_browser():
        browser.open("https://www.google.com/")
