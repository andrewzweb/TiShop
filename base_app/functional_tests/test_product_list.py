''' functional test product detail '''

import pytest
from django.urls import reverse
from .base import FunctionalTest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
import time

class ProductListTest(FunctionalTest):
    """ testcase list product """

    def setUp(self):
        ''' new setUp '''
        super(ProductListTest, self).setUp()
        self.products = mixer.cycle(5).blend('product.Product')

    @pytest.mark.integration
    def test_get_list_product_page(self):
        ''' Rob want see product page '''

        #  Rob get product
        self.browser.get(self.live_server_url +
                         reverse('product:all'))

        # Rob see 5 products in page
        # check 5 product-title
        for product in self.products:
            assert product.title in self.browser.page_source
