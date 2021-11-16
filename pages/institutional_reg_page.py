from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from fixtures.params import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


locators = {
    "business_button": (By.NAME, "company.legalName"),
    "company_button": (By.XPATH, "//input[@id='companyTypeDropdown']"),
    "other_button": (By.NAME, "company.companyTypeDetail"),
    "selected_company_locator": (By.XPATH, "//*[@class = 'css-4idjfk e5i1odf16']"),
    "county_button": (By.XPATH, "//input[@id='countryDropdown']"),
    "selected_country_locator": (By.XPATH, "//*[@class = 'css-70qvj9 e5i1odf0']"),
    "state_button": (By.XPATH, "//input[@id='stateDropdown']"),
    "selected_state_locator": (By.XPATH, "//*[@data-testid = 'stateDropdown-label']//*[@class = 'css-70qvj9 e5i1odf0']"),
    "firstname_button": (By.NAME, "personal.legalName.firstName"),
    "middlename_button": (By.NAME, "personal.legalName.middleName"),
    "lastname_button": (By.NAME, "personal.legalName.lastName"),
    "email_button": (By.NAME, "personal.email"),
    "submit_button": (By.XPATH, "//*[@data-testid = 'InstitutionSubmit']"),
    "existing_account_link": (By.XPATH, "//a[contains(text(),'Join an existing institutional account?')]"),
    "personal_information_link": (By.XPATH, "//*[@class = 'Label'][contains(text(),'Why am I providing personal information?')]"),
    "personal_information_content": (By.XPATH, "//*[@class = 'Content FreeWidth']/p"),
    "alert_box": (By.XPATH, "//*[@class = 'AlertBody']/ul"),
    "domain_alert": (By.XPATH, "//*[@class = 'AlertBody']"),
    "company_notice_locator": (By.XPATH, "//*[@class = 'companyTypeDropdown__menu css-26l3qy-menu']/div/div"),
    "country_notice_locator": (By.XPATH, "//*[@class = ' css-d57e6u']"),
    "state_notice_locator": (By.XPATH, "//*[@class = 'usStateDropdown__menu-list css-11unzgr']/div"),
}




class InstClientPage(BasePage):
    def __init__(self, driver):
        super(InstClientPage, self).__init__(driver)
        self.page_url = BASE_URL + '/register/institution'


    def enter_business_name(self, param: str) -> None:
        """
        it's used for typing into "Legal Business Name"
        :param self:
        :return none:
        """
        self.wait.until(EC.presence_of_element_located((By.NAME, locators["business_button"][1]))).send_keys(param)

    def sellect_company_type(self, param: str) -> None:
        """
        it's used for typing into "Company type"
        :param self:
        :return none:
        """
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["company_button"][1]))).send_keys(param)
        ActionChains(driver).send_keys(Keys.ENTER).perform()

    def fill_other_description(self, param:str) -> None:
        """
        it's used for typing into "Other" if we select the "Other" in "Company type"
        :param self:
        :return none:
        """
        self.wait.until(EC.presence_of_element_located((By.NAME, locators["other_button"][1]))).send_keys(param)

    def check_company_type_exist(self, param: str) -> str:
        """
          it's used for checking all types of companies in the "Company type" drop-down
          :param self:
          :return str:
        """
        driver = self.driver
        self.sellect_company_type(param)

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators["selected_company_locator"][1])))
            type = driver.find_element(By.XPATH, locators["selected_company_locator"][1]).text
        except NoSuchElementException:
            return "Locator couldn't be found"
        return type

    def select_country(self, param: str) -> None:
        """
          it's used for typing into the "Country of Business"
          :param self:
          :return none:
        """
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["county_button"][1]))).send_keys(param)
        ActionChains(driver).send_keys(Keys.ENTER).perform()

    def check_country_exist(self, param: str) -> str:
        """
          it's used for checking the countries in the "Country of Business" in the drop-down
          :param self:
          :return str:
        """
        driver = self.driver
        self.select_country(param)
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators["selected_country_locator"][1])))
            counrty = driver.find_element(By.XPATH, locators["selected_country_locator"][1]).text
        except NoSuchElementException:
            return "Locator couldn't be found"
        return counrty

    def select_state(self, param: str) -> None:
        """
          it's used for selecting the state in the "State"
          :param self:
          :return none:
        """
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["state_button"][1]))).send_keys(param)
        ActionChains(driver).send_keys(Keys.ENTER).perform()

    def check_state_exist(self, param: str) -> str:
        """
          it's used for checking the state in the "state" drop-down
          :param self:
          :return str:
        """
        driver = self.driver
        self.select_state(param)
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators["selected_state_locator"][1])))
            state = driver.find_element(By.XPATH, (locators["selected_state_locator"][1])).text
        except NoSuchElementException:
            return "Locator couldn't be found"
        return state

    def fill_legal_first_name(self, param: str) -> None:
        """
          it's used for typing into the "Legal First Name"
          :param self:
          :return none:
        """
        driver = self.driver
        driver.find_element(By.NAME, locators["firstname_button"][1]).send_keys(param)

    def fill_middle_name(self, param: str) -> None:
        """
          it's used for typing into the "Middle"
          :param self:
          :return none:
        """
        driver = self.driver
        driver.find_element(By.NAME, locators["middlename_button"][1]).send_keys(param)

    def fill_legal_last_name(self, param: str) -> None:
        """
          it's used for typing into the "Legal Last Name"
          :param self:
          :return none:
        """
        driver = self.driver
        driver.find_element(By.NAME, locators["lastname_button"][1]).send_keys(param)

    def fill_email_address(self, param: str) -> None:
        """
          it's used for typing into the "Your Email Adddress"
          :param self:
          :return none:
        """
        self.wait.until(EC.presence_of_element_located((By.NAME, locators["email_button"][1]))).send_keys(param)

    def submit_form(self) -> None:
        """
          it's used for clicking the "Continue"/"Submit" on the registration form
          :param self:
          :return none:
        """
        driver = self.driver
        element = driver.find_element(By.XPATH, (locators["submit_button"][1]))
        driver.execute_script("arguments[0].click();", element)

    def open_existing_account_link(self) -> None:
        """
          it's used for clicking to "Join an existing institutional account"
          :param self:
          :return none:
        """
        driver = self.driver
        driver.find_element(By.XPATH, (locators["existing_account_link"][1])).click()

    def get_content_of_personal_information(self) -> str:
        """
          it's used for getting the content of "Join an existing institutional account"
          :param self:
          :return str:
        """
        driver = self.driver
        driver.find_element(By.XPATH,(locators["personal_information_link"][1])).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, locators["personal_information_content"][1])))
        content = driver.find_element(By.XPATH, (locators["personal_information_content"][1])).text
        return content

    def get_alerts(self) -> list:
        """
          it's used for getting the alert/alerts when an input is empty on the registration form
          :param self
          :return list:
          """
        alert_list = []
        html_list = self.driver.find_element(By.XPATH, (locators["alert_box"][1]))
        items = html_list.find_elements_by_tag_name("li")
        for item in items:
            alert = item.text
            alert_list.append(alert)
        return alert_list

    def get_domain_alert(self) -> str:
        """
        it's used for getting the alert when input is not valid domain on the email field
        :param self
        :return str:
        """
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, locators["domain_alert"][1])))
            domain_alert = self.driver.find_element(By.XPATH, (locators["domain_alert"][1])).text
        except:
            return "Locator couldn't be found"
        return domain_alert

    def get_notice_on_company_type(self) -> str:
        """
        it's used to validating "No items found" message when invalid input is on "Company Type"
        :param self
        :return str:
        """
        driver = self.driver
        try:
            text = driver.find_element(By.XPATH, (locators["company_notice_locator"][1])).text
        except:
            return "Locator couldn't be found"
        return text


    def get_notice_on_counrty(self) -> str:
        """
        it's used to validating "No items found" message when invalid input is on "Country of Business"
        :param self:
        :return str:
        """
        driver = self.driver
        try:
            text = driver.find_element(By.XPATH,(locators["country_notice_locator"][1])).text
        except:
            return "Locator couldn't be found"
        return text

    def get_notice_on_state(self) -> str:
        """
        it's used for validating "No items found" message when invalid input on "State"
        :param self:
        :return str:
        """
        driver = self.driver
        try:
            text = driver.find_element(By.XPATH, (locators["state_notice_locator"][1])).text
        except:
            return "Locator couldn't be found"
        return text



