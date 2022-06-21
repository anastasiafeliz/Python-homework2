from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope='session', autouse=True)
def browser_size():
    browser.open('data:')
    browser.driver.set_window_size(width=1920, height=1080)
