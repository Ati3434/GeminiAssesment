from fixtures.params import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

locators = {
    "business_account_button": (By.CSS_SELECTOR, "[data-testid = 'register-go-to-institution-register']"),
    "page_body_element": (By.XPATH, "//*[@class = 'page-body Register']"),
}

class CreateAccountPage(BasePage):
    def __init__(self, driver):
        super(CreateAccountPage, self).__init__(driver)
        self.page_url = BASE_URL + '/register'

    def select_create_business_account(self) -> None:
        """
         it's used for clicking to "Create a business account"
         :param self
         :return none:
         """
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locators["business_account_button"][1]))).click()

    def verify_the_page(self) -> bool:
        """
         it's used for verifying the "create account" page is displayed"
         :param self
         :return bool:
         """
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators["page_body_element"][1])))
        except:
            return False
        else:
            return True