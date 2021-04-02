''' functional test to update product '''

import os
import time
import pytest
from django.urls import reverse
from .base import FunctionalTest
from selenium.webdriver.support.ui import Select
from product import models


class ProductUpdateTest(FunctionalTest):
    """ testcase update product """

    def setUp(self):
        ''' new setUp '''
        super(ProductUpdateTest, self).setUp()
        self.product_item = models.Product.objects.create(title='product')

    @pytest.mark.integration
    def test_update_product_add_first_product_picture(self):
        ''' Rob want add picture to product '''

        # get page where you Rob can update product
        self.browser.get(self.live_server_url +
                         reverse('product:update', kwargs={'product_slug': self.product_item.slug}))

        # write description for file
        picture_description = 'first picture'
        self.wait_for(
            self.browser.find_element_by_id('inputPictureDescription-0').send_keys(picture_description))

        # input file
        self.browser.find_element_by_id("inputPictureFile-0").send_keys(
            os.getcwd() + "/functional_tests/image.jpg")

        # click to button for update product
        self.browser.find_element_by_id('buttonUpdateProduct').click()

        # in db save Picture
        assert models.ProductImage.objects.count() == 1

        # in db first Picture have description which text Rob
        assert models.ProductImage.objects.first().description == picture_description

        # Rob see two forms for picture
        picture_description_on_page = self.wait_for(
            self.browser.find_elements_by_class_name('picture-description'))
        assert len(picture_description_on_page) == 2

        # And one of them have texted description which write Rob
        description_in_first_form = self.wait_for(
            self.browser.find_element_by_id('inputPictureDescription-0').get_attribute('value'))
        assert picture_description in description_in_first_form
