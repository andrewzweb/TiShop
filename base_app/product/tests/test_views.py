''' test views '''

from faker import Faker
import random
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import RequestFactory
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
faker = Faker()

from .. import views
from ..models import Product, ProductImage, Category

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
        assert Product.objects.count() == 5

    def test_get_page_delete_product(self):
        ''' test delete product if method show all product '''
        product = random.choice(self.products)
        req = self.req.get(reverse('product:delete', kwargs={'product_slug':product.slug}))
        resp = views.product_delete(req, product_slug=product.slug)
        assert resp.status_code == 200
        assert product.title in str(resp.content)
        assert 'Delete' in str(resp.content)
        assert Product.objects.count() == 5

    def test_send_post_to_page_delete_and_delete_product(self):
        ''' test view show all product '''
        product = random.choice(self.products)
        req = self.req.post(reverse('product:delete', kwargs={'product_slug':product.slug}))
        resp = views.product_delete(req, product_slug=product.slug)
        assert resp.status_code == 302
        assert Product.objects.count() == 4


class TestProductCreateView:
    ''' test product create view'''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()

    def test_create_product_view_return_page(self):
        ''' test create product view return page '''
        req = self.req.get(reverse('product:add'))
        resp = views.product_add(req)
        assert resp.status_code == 200


    def test_create_product_view_send_post_request(self):
        ''' test view show all product '''

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')

        req = self.req.post(
            reverse('product:add'),
            data={
                'product-title': 'Product Title',
                'product-description': 'Product Description',
                'picture-description': 'Picture Description',
                'picture-image': image,
            }
        )
        resp = views.product_add(req)
        assert resp.status_code == 302
        assert Product.objects.count() == 1


class TestProductUpdateView:
    ''' test product update view'''

    def setup(self):
        ''' set up '''
        self.req = RequestFactory()
        self.product = mixer.blend('product.Product')

        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
            b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
            b'\x02\x4c\x01\x00\x3b'
        )
        self.image = SimpleUploadedFile('small.gif', small_gif, content_type='image/gif')


    def test_get_page(self):
        ''' test create product view return page '''

        req = self.req.get(reverse('product:update', kwargs={'product_slug':self.product.slug}))
        resp = views.product_update(req, self.product.slug)
        assert resp.status_code == 200


    def test_render_form_data(self):
        '''test render form data'''

        pic1 = ProductImage.objects.create(description='pic1', image=self.image, product=self.product)
        pic2 = ProductImage.objects.create(description='pic2', image=self.image, product=self.product)
        pic3 = ProductImage.objects.create(description='pic3', image=self.image, product=self.product)
        pic4 = ProductImage.objects.create(description='pic4', image=self.image, product=self.product)
        pic5 = ProductImage.objects.create(description='pic5', image=self.image, product=self.product)
        pictures = [pic1, pic2, pic3, pic4, pic5]
        assert ProductImage.objects.count() == 5
        assert pic1.product == self.product

        req = self.req.get(
            reverse('product:update', kwargs={'product_slug':self.product.slug}))
        resp = views.product_update(req, product_slug=self.product.slug)
        for picture in pictures:
            assert picture.description in str(resp.content)


    def test_update_product_view_send_post_request(self):
        ''' test view show all product '''

        new_product_title = 'New Product Title'
        new_product_description = 'Product Description'
        picture_description = 'Picture Description'
        picture_image = self.image

        req = self.req.post(
            reverse('product:update', kwargs={'product_slug':self.product.slug}),
            data={
                'product-title': new_product_title,
                'product-description': new_product_description,
                'form-TOTAL_FORMS': 1,
                'form-INITIAL_FORMS': 0,
                'form-0-id': '',
                'form-0-description': picture_description,
                'form-0-image': picture_image,
                'form-0-DELETE': '',
            }
        )
        
        resp = views.product_update(req, product_slug=self.product.slug)
        
        assert resp.status_code == 302, 'views redirect in succses update'
        assert Product.objects.count() == 1
        assert ProductImage.objects.count() == 1
        assert Product.objects.first().title == new_product_title
        assert ProductImage.objects.first().description == picture_description
        assert ProductImage.objects.first().product == Product.objects.first()
