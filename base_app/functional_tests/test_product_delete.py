''' functional test to delete product '''

from django.urls import reverse
from mixer.backend.django import mixer
import pytest
from .base import FunctionalTest
pytestmark = pytest.mark.django_db


class ProductDeleteTest(FunctionalTest):
    """ testcase product delete  """

    @pytest.mark.integration
    def test_delete_product(self):
        ''' Rob want delete product '''

        # create product in db
        product = mixer.blend('product.Product')

        # get page where you Rob can delete
        self.browser.get(self.live_server_url +
                         reverse('product:delete', kwargs={'product_slug':product.slug}))

        # Rob find botton to delete item
        self.wait_for(self.browser.find_element_by_id('delete-button'))

        # Ro click to botton
        self.wait_for(self.browser.find_element_by_id('delete-button').click())
