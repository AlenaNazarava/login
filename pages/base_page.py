import os
import sys
import requests
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import LocatorMode
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from abc import abstractmethod
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from random import choice
from string import lowercase
from string import digits
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def refresh_page(self):
        self.driver.refresh()

    def is_element_present(self, waitTime, locatorMode, Locator):

        element = None
        try:
            if locatorMode == LocatorMode.ID:
                element = WebDriverWait(self.driver, waitTime). \
                    until(EC.visibility_of_element_located((By.ID, Locator)))
                return True
            elif locatorMode == LocatorMode.NAME:
                element = WebDriverWait(self.driver, waitTime). \
                    until(EC.visibility_of_element_located((By.NAME, Locator)))
            elif locatorMode == LocatorMode.XPATH:
                element = WebDriverWait(self.driver, waitTime). \
                    until(EC.visibility_of_element_located((By.XPATH, Locator)))
            elif locatorMode == LocatorMode.CSS_SELECTOR:
                element = WebDriverWait(self.driver, waitTime). \
                    until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))
            else:
                raise Exception("Unsupported locator strategy.")
        except NoSuchElementException:
            return False
        return element

    def wait_for_element_visibility(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_until_element_clickable(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.element_to_be_clickable((By.CSS_SELECTOR, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def find_element(self, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(Locator)
        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(Locator)
        elif locatorMode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(Locator)
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(Locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locatorMode, Locator, text):
        self.find_element(locatorMode, Locator).clear()
        self.find_element(locatorMode, Locator).send_keys(text)

    def click(self, waitTime, locatorMode, Locator):
        self.wait_until_element_clickable(waitTime, locatorMode, Locator).click()

    def check_successful_page_load(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        current_url = self.driver.current_url
        r = requests.get(current_url, verify=False)
        print r.status_code
        assert (r.status_code == 200)

    def check_error_page_load(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        current_url = self.driver.current_url
        r = requests.get(current_url, verify=False)
        assert (r.status_code == 503)


