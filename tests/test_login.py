import sys
sys.path.append("..")
from pages.homepage import Homepage
from pages.base_page import BasePage
from base_test_case import BaseTestCase
import unittest


class LoginTest(BaseTestCase, unittest.TestCase):

    def test_login(self):

        driver = self.driver
        driver.get(self.getDomain())
        Homepage_obj = Homepage(self.driver)
        Homepage_obj.user_is_on_homepage()
        Homepage_obj.login()
        Homepage_obj.successful_login()


suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
unittest.TextTestRunner(verbosity=2).run(suite)
