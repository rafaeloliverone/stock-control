from django.shortcuts import render
from .models import Stock

# Create your views here.
def stock_list(request):
    all_stock = Stock.objects.all()
    return render(request, 'stock_control/stock_list.html', {'all_stock': all_stock})