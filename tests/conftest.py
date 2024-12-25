import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import TestData


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1200,800')
    browser = webdriver.Chrome(options=options)
    browser.get(TestData.main_url)
    yield browser
    browser.quit()

