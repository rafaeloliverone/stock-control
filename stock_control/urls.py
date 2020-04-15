from django.urls import path, include
from . import views
from .views import SearchResultsView
from .views import StockUpdate

urlpatterns = [
    path('', views.stock_list, name='stock_list'),
    path('stock/create', views.stock_create, name='stock_create'),
    path('stock/<int:stock_id>/detail/', views.stock_detail, name='stock_detail'),
    path('stock/<int:pk>/edit/', StockUpdate.as_view(), name='stock_edit'),
    path('stock/<int:stock_id>/delete/', views.stock_delete, name='stock_delete'),

    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('category/new/', views.category_add, name='category_add'),
]
