import sys
sys.path.append("..")
from pages.homepage import Homepage
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

    def test_login_error(self):
        driver = self.driver
        driver.get(self.getDomain())
        Homepage_obj = Homepage(self.driver)
        Homepage_obj.user_is_on_homepage()
        Homepage_obj.login_invalid_email()
        Homepage_obj.error_login()

    def test_login_empty_fields(self):
        driver = self.driver
        driver.get(self.getDomain())
        Homepage_obj = Homepage(self.driver)
        Homepage_obj.user_is_on_homepage()
        Homepage_obj.login_empty_fields()


suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
unittest.TextTestRunner(verbosity=2).run(suite)
