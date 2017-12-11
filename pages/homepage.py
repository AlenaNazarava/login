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

        self.check_successful_page_load()
        self.wait_for_element_visibility(10, "xpath", HomePageMap['invalidEmailPasswordXPATH'])

    def login_empty_fields(self):

        self.find_element("id", HomePageMap['signUpFormID'])
        self.find_element("xpath", HomePageMap['loginLinkXPATH'])
        self.click(10, "xpath", HomePageMap['loginLinkXPATH'])
        time.sleep(5)
        self.wait_for_element_visibility(10, "xpath", HomePageMap['loginEmailXPATH'])
        self.find_element("xpath", HomePageMap['loginEmailXPATH']).clear()
        self.find_element("xpath", HomePageMap['loginPasswordXPATH']).clear()
        self.click(10, "css", HomePageMap['submitButtonCSS'])
        self.check_successful_page_load()
        # different error messages?
        self.wait_for_element_visibility(10, "xpath", HomePageMap['emptyEmailPasswordXPATH'])



