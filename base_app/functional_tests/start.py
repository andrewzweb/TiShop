from .base import FunctionalTest
from django.urls import reverse


class HomePageTest(FunctionalTest):
    """ test new user """

    def test_get_home_page(self):
        self.browser.get(self.live_server_url)
        assert 'Home' in self.browser.title
