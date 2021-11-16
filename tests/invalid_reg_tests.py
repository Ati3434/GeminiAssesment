import random
import pytest
from fixtures.base import Base
from pages.login_page import LoginPage
from pages.create_accocunt_page import CreateAccountPage
from pages.institutional_reg_page import InstClientPage
from pages.thanks_reg_page import ThanksRegPage
from tests.valid_reg_tests import COMPANY_TYPES, COUNTRIES, STATES

INVALID_DOMAINS = ["0", "name", "name@gmailcom", "@gmail.com", "@hotmail.com","nameatgmail.com", "name@11", "name@yahoo,com"]
INVALID_EMAILS = ["name@gmail.com1", "name@gmail..com1", "name@hotmail.2com"]


class InvalidTestCases(Base):
    def setUp(self):
        super(InvalidTestCases, self).setUp()
        self.login = LoginPage(self.driver)
        self.login.go_to_page()
        self.create_an_account = CreateAccountPage(self.driver)
        self.inst_registration = InstClientPage(self.driver)
        self.thanks_page = ThanksRegPage(self.driver)
        self.login.select_create_new_account()
        self.create_an_account.select_create_business_account()

    # @pytest.mark.skip
    # verify that required default fields are in the Alert
    def test_verify_alerts(self):
        self.inst_registration.submit_form()
        actualAlerts = self.inst_registration.get_alerts()

        expected_alerts = [
            "Legal Business Name is required.", "Company type is required.", "First name is required.",
            "Last name is required.", "Please enter a valid email address.", "Company state is required."
        ]

        for alert in expected_alerts:
            if alert not in actualAlerts:
                self.assertEqual(alert, False, f"alert [{alert}] doesn't appear in the alert box")

    # @pytest.mark.skip
    #Verify that "No items found" appear for "Company type" when input is not in the drop-down
    def test_notice_company(self):
        self.inst_registration.sellect_company_type("CompanyTypeXXX")
        actualNotice = self.inst_registration.get_notice_on_company_type()
        print(actualNotice)
        self.assertEqual("No items found.", actualNotice)

    # @pytest.mark.skip
    #Verify that "No items found" appear for "Country of Business" when input is not in the drop-down
    def test_notice_country(self):
        self.inst_registration.select_country("CountryXXX")
        actualNotice = self.inst_registration.get_notice_on_counrty()
        self.assertEqual("No items found.", actualNotice)

    # @pytest.mark.skip
    # Verify that "No items found" appear for "State" when input is not in the drop-down
    def test_notice_state(self):
        self.inst_registration.sellect_company_type("United States")
        self.inst_registration.select_state("StateXXX")
        actualNotice = self.inst_registration.get_notice_on_company_type()
        self.assertEqual("No items found.", actualNotice)

    # @pytest.mark.skip
    #Check submitting form by not filling required field, "Legal Business Name"
    def test_reg_empty_lbn(self):
        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        randomCountry = random.choice(COUNTRIES)
        if randomCountry == "United States":
            self.inst_registration.select_country(randomCountry)
            self.inst_registration.select_state(random.choice(STATES))
        else:
            self.inst_registration.select_country(randomCountry)

        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.fill_email_address("bowie_dave@gmail.com")
        self.inst_registration.submit_form()

        alerts = self.inst_registration.get_alerts()
        self.assertIn("Legal Business Name is required.", alerts)

    # @pytest.mark.skip
    #Check the submitting form by not filling required field, "Company Type"
    def test_reg_empty_company(self):
        self.inst_registration.enter_business_name("BRG-Test investment05")

        randomCountry = random.choice(COUNTRIES)
        if randomCountry == "United States":
            self.inst_registration.select_country(randomCountry)
            self.inst_registration.select_state(random.choice(STATES))
        else:
            self.inst_registration.select_country(randomCountry)

        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.fill_email_address("bowie_dave@gmail.com")
        self.inst_registration.submit_form()

        alerts = self.inst_registration.get_alerts()
        self.assertIn("Company type is required.", alerts)

    # @pytest.mark.skip
    #Check the submitting form by not filling required field, "State"
    def test_reg_empty_state(self):
        self.inst_registration.enter_business_name("BRG-Test investment06")

        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        self.inst_registration.select_country("United States")
        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.fill_email_address("bowie_dave@gmail.com")
        self.inst_registration.submit_form()

        alerts = self.inst_registration.get_alerts()
        self.assertIn("Company state is required.", alerts)

    # @pytest.mark.skip
    # Check the submitting form by not filling required field, "Legal First Name"
    def test_reg_empty_firstname(self):
        self.inst_registration.enter_business_name("BRG-Test investment07")

        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        randomCountry = random.choice(COUNTRIES)
        if randomCountry == "United States":
            self.inst_registration.select_country(randomCountry)
            self.inst_registration.select_state(random.choice(STATES))
        else:
            self.inst_registration.select_country(randomCountry)

        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.fill_email_address("bowie_dave@gmail.com")
        self.inst_registration.submit_form()

        alerts = self.inst_registration.get_alerts()
        self.assertIn("First name is required.", alerts)

    # @pytest.mark.skip
    #Check submitting form by not filling required field, "Legal last Name"
    def test_reg_empty_lastname(self):
        self.inst_registration.enter_business_name("BRG-Test investment08")

        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        randomCountry = random.choice(COUNTRIES)
        if randomCountry == "United States":
            self.inst_registration.select_country(randomCountry)
            self.inst_registration.select_state(random.choice(STATES))
        else:
            self.inst_registration.select_country(randomCountry)

        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_email_address("bowie_dave@gmail.com")
        self.inst_registration.submit_form()

        alerts = self.inst_registration.get_alerts()
        self.assertIn("Last name is required.", alerts)

    # @pytest.mark.skip
    # Check submitting form by not filling required field, "Email Address"
    def test_reg_empty_email(self):
        self.inst_registration.enter_business_name("BRG-Test investment09")

        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        randomCountry = random.choice(COUNTRIES)
        if randomCountry == "United States":
            self.inst_registration.select_country(randomCountry)
            self.inst_registration.select_state(random.choice(STATES))
        else:
            self.inst_registration.select_country(randomCountry)

        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.submit_form()

        alerts = self.inst_registration.get_alerts()
        self.assertIn("Please enter a valid email address.", alerts)

    # @pytest.mark.skip
    # Check submitting form by invalid email domains
    def test_invalid_email_domain(self):
        for email in INVALID_DOMAINS:
            self.inst_registration.enter_business_name("BRG-Test investment09")

            randomType = random.choice(COMPANY_TYPES)
            if randomType == "Other":
                self.inst_registration.sellect_company_type(randomType)
                self.inst_registration.fill_other_description("Joint Venture")
            else:
                self.inst_registration.sellect_company_type(randomType)

            randomCountry = random.choice(COUNTRIES)
            if randomCountry == "United States":
                self.inst_registration.select_country(randomCountry)
                self.inst_registration.select_state(random.choice(STATES))
            else:
                self.inst_registration.select_country(randomCountry)

            self.inst_registration.fill_legal_first_name("Dave")
            self.inst_registration.fill_legal_last_name("Bowie")
            self.inst_registration.fill_email_address(email)
            self.inst_registration.submit_form()
            alert = self.inst_registration.get_domain_alert()
            self.assertEqual("Please specify a valid email domain.", alert, f"{email} type doesn't have an expected alert")
            self.driver.refresh()

    # @pytest.mark.skip
    # Check submitting form by invalid email addresses
    def test_invalid_email_address(self):
        for email in INVALID_EMAILS:
            self.inst_registration.enter_business_name("BRG-Test investment09")

            randomType = random.choice(COMPANY_TYPES)
            if randomType == "Other":
                self.inst_registration.sellect_company_type(randomType)
                self.inst_registration.fill_other_description("Joint Venture")
            else:
                self.inst_registration.sellect_company_type(randomType)

            randomCountry = random.choice(COUNTRIES)
            if randomCountry == "United States":
                self.inst_registration.select_country(randomCountry)
                self.inst_registration.select_state(random.choice(STATES))
            else:
                self.inst_registration.select_country(randomCountry)

            self.inst_registration.fill_legal_first_name("Dave")
            self.inst_registration.fill_legal_last_name("Bowie")
            self.inst_registration.fill_email_address(email)
            self.inst_registration.submit_form()
            alert = self.inst_registration.get_domain_alert()
            self.assertEqual("Please use a valid email address.", alert, f"{email} doesn't have an expected alert")
            self.driver.refresh()

    #Invalid test cases should be expanded to other fields. Such as, "Legal Business Name", "Legal First Name", "Legal Last Name"
    #Currently all other fields accept any condition as an input. Specifications need to be clearify for these fields
