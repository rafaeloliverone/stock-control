from django.test import SimpleTestCase
from django.urls import reverse, resolve

from stock_control.views import stock_list, stock_create, stock_detail 
from ..views import StockUpdate

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('stock_list')
        self.assertEquals(resolve(url).func, stock_list)

    def test_stock_create_url_is_resolved(self):
        url = reverse('stock_create')
        self.assertEquals(resolve(url).func, stock_create)

    def test_stock_detail_url_is_resolved(self):
        arg = 1
        url = reverse('stock_detail', args=[arg])
        self.assertEquals(resolve(url).func, stock_detail)
    
    def test_stock_edit_url_resolve_with_StockUpdate(self):
        arg = 2
        url = reverse('stock_edit', args=[arg])
        self.assertEquals(url, '/stock/2/edit/')
    
