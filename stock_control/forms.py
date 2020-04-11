from django import forms

from .models import Category
from .models import Stock


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'description',)


class StockForm(forms.ModelForm):

    class Meta:
        model = Stock
        fields = '__all__'
