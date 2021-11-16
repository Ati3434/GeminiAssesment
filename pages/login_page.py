from fixtures.params import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

locators = {
    "create_new_account": (By.CSS_SELECTOR, "[data-testid = 'goToRegister']"),
}

class LoginPage(BasePage):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.page_url = BASE_URL

    def select_create_new_account(self) -> None:
        """
         it's used for clicking to "Create new account"
         :param self
         :return none:
         """
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators["create_new_account"][1]))).click()




