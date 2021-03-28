''' functional test product detail '''

import pytest
from django.urls import reverse
from .base import FunctionalTest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class ProductDetailTest(FunctionalTest):
    """ testcase detail product """

    def setUp(self):
        ''' new setUp '''
        super(ProductDetailTest, self).setUp()

        self.product_title = 'Product Title'
        self.product_description = 'description'
        self.product_price = 120

        self.product = mixer.blend('product.Product',
            title=self.product_title,
            description=self.product_description,
            price=self.product_price
        )

    @pytest.mark.integration
    def test_get_detail_page(self):
        ''' Rob want see product page '''

        #  Rob get product
        self.browser.get(self.live_server_url +
                         reverse('product:detail',
                                 kwargs={'product_slug': self.product.slug}))

        # Rob see product title
        created_product_title = self.wait_for(
            self.browser.find_element_by_id('product-title').text)

        # it's the same product-title
        assert created_product_title == self.product_title

        # Rob check prise
        created_product_price = self.wait_for(
            self.browser.find_element_by_id('product-price').text)
        assert str(self.product_price) in created_product_price

        # Rob check description
        created_product_description = self.wait_for(
            self.browser.find_element_by_id('product-description').text)
        assert self.product_description in created_product_description
