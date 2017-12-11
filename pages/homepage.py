import sys
from base_page import BasePage
sys.path.append("..")
from core.ui_map import HomePageMap
import time


# import pdb;
# pdb.set_trace()

class Homepage(BasePage):

    def __init__(self, driver):
        super(Homepage, self).__init__(driver)

    def user_is_on_homepage(self):
        self.wait_for_element_visibility(10, "id", HomePageMap['signUpFormID'])
        self.is_element_present(5, "xpath", HomePageMap['signUpTextXPATH'])

    def fill_out_signup_form(self):

        self.find_element("id", HomePageMap['signUpFormID'])
        self.is_element_present(5, "xpath", HomePageMap['signUpFirstNameXPATH'])
        self.find_element("xpath", HomePageMap['signUpFirstNameXPATH']).clear()
        self.find_element("xpath", HomePageMap['signUpFirstNameXPATH']).send_keys(self.random_string)
        self.find_element("xpath", HomePageMap['signUpLastNameXPATH']).clear()
        self.find_element("xpath", HomePageMap['signUpLastNameXPATH']).send_keys(self.random_string)
        self.find_element("xpath", HomePageMap['signUpEmailXPATH']).clear()
        self.find_element("xpath", HomePageMap['signUpEmailXPATH']).send_keys(self.random_email())
        self.find_element("xpath", HomePageMap['signUpPasswordXPATH']).clear()
        self.find_element("xpath", HomePageMap['signUpPasswordXPATH']).send_keys(self.random_string)
        self.click(10, "id", HomePageMap['signUpCheckboxTermsConditionsID'])
        self.click(10, "css", HomePageMap['signUpCreateAccountButtonCSS'])

    def login(self):

        self.find_element("id", HomePageMap['signUpFormID'])
        self.find_element("xpath", HomePageMap['loginLinkXPATH'])
        self.click(10, "xpath", HomePageMap['loginLinkXPATH'])
        time.sleep(5)
        self.wait_for_element_visibility(10, "xpath", HomePageMap['loginEmailXPATH'])
        self.find_element("xpath", HomePageMap['loginEmailXPATH']).clear()
        self.find_element("xpath", HomePageMap['loginEmailXPATH']).send_keys(HomePageMap['emailTEXT'])
        self.find_element("xpath", HomePageMap['loginPasswordXPATH']).clear()
        self.find_element("xpath", HomePageMap['loginPasswordXPATH']).send_keys(HomePageMap['passwordTEXT'])
        self.click(10, "css", HomePageMap['submitButtonCSS'])

    def successful_login(self):

        self.check_successful_page_load()
        self.wait_for_element_visibility(10, "xpath", HomePageMap['welcomTextXPATH'])

    def login_invalid_email(self):

        self.find_element("id", HomePageMap['signUpFormID'])
        self.find_element("xpath", HomePageMap['loginLinkXPATH'])
        self.click(10, "xpath", HomePageMap['loginLinkXPATH'])
        time.sleep(5)
        self.wait_for_element_visibility(10, "xpath", HomePageMap['loginEmailXPATH'])
        self.find_element("xpath", HomePageMap['loginEmailXPATH']).clear()
        self.find_element("xpath", HomePageMap['loginEmailXPATH']).send_keys(HomePageMap['emailIncorrectTEXT'])
        self.find_element("xpath", HomePageMap['loginPasswordXPATH']).clear()
        self.find_element("xpath", HomePageMap['loginPasswordXPATH']).send_keys(HomePageMap['passwordTEXT'])
        self.click(10, "css", HomePageMap['submitButtonCSS'])

    def error_login(self):

        self.check_error_page_load()
        self.wait_for_element_visibility(10, "xpath", HomePageMap['invalidEmailPasswordXPATH'])
