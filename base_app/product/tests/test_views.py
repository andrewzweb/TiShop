''' test views '''

import random
import pytest
from django.urls import reverse
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from .. import views
from .. import models

class TestHome:
    ''' test home view '''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()

    def test_get_home_view(self):
        ''' test get home view '''
        resp = views.home(self.req)
        assert resp.status_code == 200

    def test_show_greatings_in_view(self):
        ''' test show greatings in view '''
        resp = views.home(self.req)
        greatings = 'Hello you are at home'
        assert greatings in str(resp.content)


class TestProductListView:
    ''' testcase product list'''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()
        self.products = mixer.cycle(5).blend('product.Product')

    def test_get_product_list(self):
        ''' test get product list '''
        resp = views.product_all(self.req)
        assert resp.status_code == 200

    def test_view_show_all_product(self):
        ''' test view show all product '''
        resp = views.product_all(self.req)
        for product in self.products:
            assert product.title in str(resp.content)
            assert product.slug in str(resp.content)
            assert str(product.price) in str(resp.content)


class TestProductDetailView:
    ''' test product detail view'''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory
        self.products = mixer.cycle(5).blend('product.Product')

    def test_get_product_detail(self):
        ''' test view show all product '''
        product = random.choice(self.products)
        resp = views.product_detail(self.req, product_slug=product.slug)
        assert product.title in str(resp.content)
        assert str(product.price) in str(resp.content)


class TestProductDeleteView:
    ''' test product delete view'''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()
        self.products = mixer.cycle(5).blend('product.Product')
        assert models.Product.objects.count() == 5

    def test_get_page_delete_product(self):
        ''' test delete product if method show all product '''
        product = random.choice(self.products)
        req = self.req.get(reverse('product:delete', kwargs={'product_slug':product.slug}))
        resp = views.product_delete(req, product_slug=product.slug)
        assert resp.status_code == 200
        assert product.title in str(resp.content)
        assert 'Delete' in str(resp.content)
        assert models.Product.objects.count() == 5

    def test_send_post_to_page_delete_and_delete_product(self):
        ''' test view show all product '''
        product = random.choice(self.products)
        req = self.req.post(reverse('product:delete', kwargs={'product_slug':product.slug}))
        resp = views.product_delete(req, product_slug=product.slug)
        assert resp.status_code == 302
        assert models.Product.objects.count() == 4
