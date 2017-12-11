from constants import hh_constants
from selenium import webdriver
import os


class BaseTestCase(object):

    def getDomain(self):
        try:
            testDomain = os.environ['TEST_SUBJECT_DOMAIN']
        except:
            testDomain = 'localhost'
        return 'https://' + testDomain

    def setUp(self):
        if hh_constants['Browser'].lower() == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
        elif hh_constants['Browser'].lower() == "chrome":
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
        else:
            raise Exception("This browser is not supported at the moment.")

