from django.contrib import admin
from .models import Stock
from .models import Category

admin.site.register(Stock)
admin.site.register(Category)
