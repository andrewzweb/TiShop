''' functional test to create product '''

import os
import time
import pytest
from django.urls import reverse
from .base import FunctionalTest
from selenium.webdriver.support.ui import Select
from product import models


class ProductCreateTest(FunctionalTest):
    """ testcase create product """

    def setUp(self):
        ''' new setUp '''
        super(ProductCreateTest, self).setUp()
        models.Category.objects.create(title='product')

    @pytest.mark.integration
    def test_create_product(self):
        ''' Rob want create product '''

        # get page where you Rob can create product
        self.browser.get(self.live_server_url +
                         reverse('product:add'))

        # write title of product
        product_title = 'product'
        self.wait_for(self.browser.find_element_by_id('inputProductTitle').send_keys(product_title))

        # write desctiprion
        product_description = 'description'
        self.browser.find_element_by_id('inputProductDescription').send_keys(product_description)

        # set price
        product_price = '100'
        self.browser.find_element_by_id('inputProductPrice').clear()
        self.browser.find_element_by_id('inputProductPrice').send_keys(product_price)

        # select category
        select = Select(self.browser.find_element_by_id('inputProductCategorySelect'))

        # select by visible text
        select.select_by_visible_text('product')

        # write image description
        self.browser.find_element_by_id('inputPictureDescription').send_keys('image-description')

        # select image
        self.browser.find_element_by_id("inputPictureFile").send_keys(
            os.getcwd() + "/functional_tests/image.jpg")

        # click to button for add product
        self.browser.find_element_by_id('buttonAddProduct').click()

        # and then we get page with this product

#        # Rob see product title
#        created_product_title = self.wait_for(
#            self.browser.find_element_by_id('product-title').text)
#
#        # it's the same product-title
#        assert created_product_title == product_title
#
#        # Rob check prise
#        created_product_price = self.wait_for(
#            self.browser.find_element_by_id('product-price').text)
#        assert product_price in created_product_price
#
#        # Rob check description
#        created_product_description = self.wait_for(
#            self.browser.find_element_by_id('product-description').text)
#        assert product_description in created_product_description
