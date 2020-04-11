from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .models import Stock
from .forms import CategoryForm
from .forms import StockForm

# Create your views here.


def stock_list(request):
    stock = Stock.objects.all()
    all_stock = Paginator(stock, 2)

    page_number = request.GET.get('page')
    page_obj = all_stock.get_page(page_number)
    return render(request, 'stock_control/stock_list.html', {
        'all_stock': page_obj,
        'range_pages': range(1, page_obj.paginator.num_pages+1)
    })


def stock_add(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.save()
            return redirect('/')
    else:
        form = StockForm()

    return render(request, 'stock_control/stock_add.html', {'form': form})


def category_add(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('/')
    else:
        category = CategoryForm()

    return render(request, 'category/category_add.html', {'category': category})
