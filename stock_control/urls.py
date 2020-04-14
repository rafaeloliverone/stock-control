from django.urls import path, include
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('stock/new', views.stock_add, name='stock_add'),
    path('stock/<int:stock_id>/detail/', views.stock_detail, name='stock_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    path('category/new/', views.category_add, name='category_add'),
]
