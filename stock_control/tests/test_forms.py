from django.test import TestCase
from model_bakery import baker
from datetime import date

from stock_control.models import Category
from ..forms import CategoryForm


class CategoryFormTestCase(TestCase):

    def test_category_form_valid(self):
        form = CategoryForm(data={
            'name': 'Automoveis Elétricos',
            'description': 'Automoveis que recarregam na energia'
        })
        self.assertTrue(form.is_valid())

    def test_category_form_invalid(self):
        form = CategoryForm(data={})
        self.assertFalse(form.is_valid())
