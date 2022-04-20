from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
