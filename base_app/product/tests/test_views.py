import pytest 
from django.urls import reverse
from django.test import RequestFactory

from .. import views


class TestHome:
    ''' test home view '''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory
        
    def test_get_home_view(self):
        ''' test get home view '''
        resp = views.home(self.req)
        assert resp.status_code == 200

    def test_show_greatings_in_view(self):
        ''' test show greatings in view '''
        resp = views.home(self.req)
        greatings = 'Hello you are at home'
        assert greatings in str(resp.content)
