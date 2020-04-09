from django.test import TestCase 
from model_bakery import baker   

from django.utils import timezone
import pytz

from stock_control.models import Stock

class StockTestCase(TestCase):

    def setUp(self):
        self.stock = Stock.objects.create(
            name='Car',
            quantity=10,
            unitary_value=120,
            created_date=timezone.now(),
            published_date=timezone.now(),
        )

    def test_return_str(self):
        stock = Stock.objects.get(name='Car')
        self.assertEquals(stock.__str__(), 'Car')