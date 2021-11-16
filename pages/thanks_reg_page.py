from fixtures.params import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

locators = {
    "thanks_message": (By.XPATH, "//*[@class = 'NarrowTitle']/.")
}

class ThanksRegPage(BasePage):
    def __init__(self, driver):
        super(ThanksRegPage, self).__init__(driver)
        self.page_url = BASE_URL + "/register/institution/thanks"

    def get_thanks_message(self) -> str:
        """
        it's used for verifying the "thanks for registering!" page
        :param self:
        :return str:
        """
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["thanks_message"][1])))
        message = driver.find_element(By.XPATH, (locators["thanks_message"][1])).text
        return message
