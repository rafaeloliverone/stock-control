from django.test import SimpleTestCase
from django.urls import reverse, resolve

from stock_control.views import stock_list, stock_add

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('stock_list')
        self.assertEquals(resolve(url).func, stock_list)