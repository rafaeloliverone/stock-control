from django.test import TestCase, Client
from django.urls import reverse
from model_bakery import baker
from pprint import pprint
import json

from ..models import Stock, Category

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.stock_list = reverse('stock_list')
        
        self.stock = baker.make(Stock)
        self.stock.category = baker.make(Category)
        # pprint(self.stock.__dict__)

    def test_stock_index_GET(self):
        response = self.client.get(self.stock_list)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'stock_control/stock_list.html')