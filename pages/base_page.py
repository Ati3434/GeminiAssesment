from fixtures.params import EXPLICIT_TIMEOUT
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, EXPLICIT_TIMEOUT)
        self.page_url = None

    def go_to_page(self):
        self.driver.get(self.page_url)

