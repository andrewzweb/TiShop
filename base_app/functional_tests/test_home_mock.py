from .base import FunctionalTest
from django.urls import reverse
import pytest

class HomePageTest(FunctionalTest):
    """ testcase home view """

    @pytest.mark.integration
    def test_get_home_page(self):
        ''' test get home page '''
        self.browser.get(
            self.live_server_url + reverse('product:home'))
        assert 'Home' in self.browser.title
