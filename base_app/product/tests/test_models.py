''' Test product models '''

import decimal
import pytest
from django.utils.text import slugify
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

from ..models import ProductImage

class TestProduct:
    ''' test product '''

    def setup(self):
        '''set up'''
        self.product = mixer.blend('product.Product')

    def test_product_model_exist(self):
        ''' test model exist '''
        assert self.product.id == 1, 'Should create a Product instance with id 1'

    def test_product_have_title(self):
        ''' test product have title '''
        product = mixer.blend('product.Product', title='product title')
        assert product.title == 'product title'

    def test_product_have_slug(self):
        '''test product have slug'''
        assert self.product.slug

    def test_product_slug_its_title(self):
        '''test product slug its title'''
        assert self.product.slug == slugify(self.product.title)

    def test_product_have_description(self):
        '''test product have description'''
        product = mixer.blend('product.Product', description='product description')
        assert product.description == 'product description'

    def test_product_have_price(self):
        '''test product have price'''
        product = mixer.blend('product.Product', price=10.00)
        assert product.price == 10.00

    def test_product_price_default_is_zero(self):
        '''test product price default is zero'''
        product = mixer.blend('product.Product')
        assert product.price == 0

    def test_product_price_max_number_max_is_ten_digits(self):
        '''test product price max number max is ten digits'''
        with pytest.raises(decimal.InvalidOperation):
            mixer.blend('product.Product', price=100000000.00)

    def test_product_price_have_decimal_places(self):
        '''test product price have decimal places'''
        product = mixer.blend('product.Product', price=1)
        assert product.price == decimal.Decimal(1.00)

    def test_product_str_return_title(self):
        '''test product str return title'''
        product = mixer.blend('product.Product')
        assert product.title in str(product)


class TestProductImage:
    ''' testcase product image '''

    def setup(self):
        ''' setup '''
        self.product = mixer.blend('product.Product')
        self.product_image = mixer.blend('product.ProductImage', product=self.product)

    def test_exist_product_image(self):
        '''test exist product image'''
        assert ProductImage.objects.count() == 1

    def test_obj_have_description(self):
        '''test obj have description'''
        assert self.product_image.description

    def test_obj_have_image(self):
        '''test obj have image'''
        assert self.product_image.image

    def test_obj_have_ralation_with_product(self):
        '''test obj have ralation with product'''
        assert self.product_image.product == self.product

    def test_obj_str_return_title(self):
        '''test obj str return title'''
        assert str(self.product_image) == self.product_image.description

    def test_obj_small_image(self):
        '''test obj small image'''
        assert self.product_image.image.url in  self.product_image.small_image()


class TestCategory:
    ''' testcase category'''

    def setup(self):
        self.product = mixer.blend('product.Product')
        self.category = mixer.blend('product.Category', product=self.product)
    
    def test_category_exist(self):
        ''' test category '''
        assert self.category

    def test_category_have_title(self):
        '''test category have title'''
        assert self.category.title

    def test_category_have_slug(self):
        '''test category have slug'''
        assert self.category.slug

    def test_category_method_str(self):
        '''test category have slug'''
        assert self.category.title in str(self.category)

    def test_method_save_autochange_slug(self):
        '''test category have slug'''

        # get title
        title = self.category.title
        # check slug it ccover title
        assert str(slugify(title)) == self.category.slug

        # set new title
        new_title = 'New title'
        self.category.title = new_title

        # check new title not even slug
        assert str(slugify(new_title)) != str(self.category.slug)

        # action save instance
        self.category.save()

        # check slug must be same with title
        assert str(slugify(new_title)) == str(self.category.slug)
