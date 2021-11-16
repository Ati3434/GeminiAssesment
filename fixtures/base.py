import unittest
from selenium import webdriver
from fixtures.params import CHROME_EXECUTABLE_PATH, BROWSER_TYPE, FIREFOX_EXECUTABLE_PATH, SAFARI_EXECUTABLE_PATH, EDGE_EXECUTABLE_PATH


class Base(unittest.TestCase):
    def get_browser(self):
        if BROWSER_TYPE.lower().find('chrome') >= 0:
            return webdriver.Chrome(executable_path= CHROME_EXECUTABLE_PATH)

        elif BROWSER_TYPE.lower().find('safari') >= 0:
            return webdriver.Safari(executable_path= SAFARI_EXECUTABLE_PATH)

        elif BROWSER_TYPE.lower().find('firefox') >= 0:
            return webdriver.Firefox(executable_path= FIREFOX_EXECUTABLE_PATH)

        elif BROWSER_TYPE.lower().find('edge') >= 0:
            return webdriver.Firefox(executable_path= EDGE_EXECUTABLE_PATH)

    def setUp(self):
        self.driver = self.get_browser()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()




if __name__ == '__main__':
    unittest.main()
