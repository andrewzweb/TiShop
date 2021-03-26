''' base module which use in functional tests'''

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import os

MAX_WAIT = 10

class FunctionalTest(StaticLiveServerTestCase):
    """ test new user """

    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server: 
            self.live_server_url = 'http://' + staging_server
        
    def tearDown(self):
        self.browser.quit()


    def wait(fn):
        ''' wait str in table '''

        def modified_fn(*args,**kwargs):
            start_time = time.time()
            while True:
                try: 
                    return fn(*args,**kwargs)
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn

    @wait
    def wait_for(self, fn):
        return fn
