import sys
from base_page import BasePage
sys.path.append("..")
from core.ui_map import HomePageMap
import time


# import pdb;
# pdb.set_trace()

class Signup(BasePage):

    def __init__(self, driver):
        super(Signup, self).__init__(driver)

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

