''' base module which use in functional tests'''

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(StaticLiveServerTestCase):
    """ test new user """

    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
