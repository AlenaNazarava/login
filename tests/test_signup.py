import sys
sys.path.append("..")
from pages.signup import Signup
from base_test_case import BaseTestCase
import unittest


class SignupTest(BaseTestCase, unittest.TestCase):

    def test_signup(self):

        driver = self.driver
        driver.get(self.getDomain())
        Signup_obj = Signup(self.driver)
        Signup_obj.user_is_on_homepage()
        Signup_obj.fill_out_signup_form()


suite = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
unittest.TextTestRunner(verbosity=2).run(suite)
