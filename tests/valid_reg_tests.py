import unittest
import random
import pytest as pytest
from fixtures.base import Base
from pages.login_page import LoginPage
from pages.create_accocunt_page import CreateAccountPage
from pages.institutional_reg_page import InstClientPage
from pages.thanks_reg_page import ThanksRegPage

COMPANY_TYPES = [
    "Broker-Dealer", "Money Services Business or Money Transmitter", "Non-Profit Organization",
    "Operating Company", "Personal/Private Investment Vehicle",
    "Pooled Investment Fund (Hedge Fund, Private Equity Fund, Venture Capital Fund)",
    "Professional Service Provider (Professional Accounting/Law Firm)",
    "Profit Sharing/Pension/Retirement Plan (Employer-Sponsored; not individual IRA)",
    "Publicly-traded Company", "Registered Investment Firm", "Trust", "Other"
]

COUNTRIES = [
    "United States","Afghanistan","Bahamas, The", "Cambodia", "Denmark", "El Salvador",
    "Falkland Islands (Islas Malvinas)", "Gabon", "Haiti", "Iceland", "Jamaica", "South Korea",
    "Kazakhstan", "North Korea", "Taiwan", "Uganda", "Vanuatu", "Wallis et Futuna", "Yemen", "Zambia"
]

STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "GU", "HI", "ID", "IL",
    "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV",
    "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "PR", "RI", "SC", "SD", "TN",
    "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY"
]

class ValidRegCases(Base):
    def setUp(self):
        super(ValidRegCases, self).setUp()
        self.login = LoginPage(self.driver)
        self.login.go_to_page()
        self.create_an_account = CreateAccountPage(self.driver)
        self.inst_registration = InstClientPage(self.driver)
        self.thanks_page = ThanksRegPage(self.driver)
        self.login.select_create_new_account()
        self.create_an_account.select_create_business_account()

    # @pytest.mark.skip
    # Verify that all company types exist in the "Company type" drop-down
    def test_verify_company_types(self):
        for company_type in COMPANY_TYPES :
            actual_result = self.inst_registration.check_company_type_exist(company_type)
            self.assertEqual(company_type, actual_result, f"[Company Type] doesn't have the [{company_type}] in the drop-down")
            self.driver.refresh()

    # @pytest.mark.skip
    # Verify that all countries exist in the "Country of Business" drop-down
    def test_verify_countries(self):
        for country in COUNTRIES:
            actual_result = self.inst_registration.check_country_exist(country)
            self.assertEqual(country, actual_result, f"[Country of Business] doesn't have the [{country}] in the drop-down")
            self.driver.refresh()

    # @pytest.mark.skip
    # Verify that all states exist in the "State" drop-down
    def test_verify_states(self):
        for state in STATES:
            actual_result = self.inst_registration.check_state_exist(state)
            self.assertEqual(state, actual_result, f"[State] doesn't have the [{state}] in the drop-down")
            self.driver.refresh()

    # @pytest.mark.skip
    #Verify that "existing institutional account link" works
    def test_inst_account_link(self):
        self.inst_registration.open_existing_account_link()

        actual_result = self.create_an_account.verify_the_page()
        self.assertEqual(True, actual_result)

    # @pytest.mark.skip
    #Verify that the "providing personal information?" content
    def test_providing_personal_info(self):
        expected_result = """We require the signers of an institutional account 
        to submit personal identifying information so that they can be vetted 
        through our compliance KYC protocol. Keeping your personal information secure is extremely important to us. 
        We transmit over encrypted SSL directly to our compliance team.""".replace('\n        ', "")

        actual_result = self.inst_registration.get_content_of_personal_information()
        self.assertEqual(expected_result, actual_result)

    # @pytest.mark.skip
    #Verify that gogin with selecting the company type "Other"
    def test_valid_login01(self):
        self.inst_registration.enter_business_name("BRG-Test investment01")
        self.inst_registration.sellect_company_type("Other")
        self.inst_registration.fill_other_description("Joint Venture")
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

        actual_result = self.thanks_page.get_thanks_message()
        self.assertEqual("Thanks for Registering!", actual_result)

    # @pytest.mark.skip
    #Verify that login with selecting a state
    def test_valid_login02(self):
        self.inst_registration.enter_business_name("BRG-Test investment02")
        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        self.inst_registration.select_country("United States")
        self.inst_registration.select_state(random.choice(STATES))
        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_middle_name("Santos")
        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.fill_email_address("bowie_dave@xxx.com")
        self.inst_registration.submit_form()

        actual_result = self.thanks_page.get_thanks_message()
        self.assertEqual("Thanks for Registering!", actual_result)

    # @pytest.mark.skip
    #Verify that login without selecting a state
    def test_valid_login03(self):
        self.inst_registration.enter_business_name("BRG-Test investment03")
        randomType = random.choice(COMPANY_TYPES)
        if randomType == "Other":
            self.inst_registration.sellect_company_type(randomType)
            self.inst_registration.fill_other_description("Joint Venture")
        else:
            self.inst_registration.sellect_company_type(randomType)

        self.inst_registration.select_country("Turkey")
        self.inst_registration.fill_legal_first_name("Dave")
        self.inst_registration.fill_middle_name("Santos")
        self.inst_registration.fill_legal_last_name("Bowie")
        self.inst_registration.fill_email_address("bowie_dave@hotmail.com")
        self.inst_registration.submit_form()

        actual_result = self.thanks_page.get_thanks_message()
        self.assertEqual("Thanks for Registering!", actual_result)


    # @pytest.mark.skip
    #Verify that login with empty optional middle name
    def test_valid_login04(self):
        self.inst_registration.enter_business_name("BRG-Test investment04")

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

        actual_result = self.thanks_page.get_thanks_message()
        self.assertEqual("Thanks for Registering!", actual_result)










if __name__ == '__main__':
    unittest.main()