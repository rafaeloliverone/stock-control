from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
# from django.views.generic import TemplateView, ListView
from django.views.generic.list import ListView

from .models import Stock
from .forms import CategoryForm
from .forms import StockForm

# Create your views here.

class SearchResultsView(ListView):
    model = Stock
    template_name = 'stock_control/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Stock.objects.filter(
            name__contains=query
        )
        return object_list


def stock_list(request):
    stock = Stock.objects.all()
    all_stock = Paginator(stock, 3)

    page_number = request.GET.get('page')
    page_obj = all_stock.get_page(page_number)
    return render(request, 'stock_control/stock_list.html', {
        'all_stock': page_obj,
        'range_pages': range(1, page_obj.paginator.num_pages+1)
    })

@login_required
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


@login_required
def stock_detail(request, stock_id):
    stock = get_object_or_404(Stock ,id=stock_id)
    return render(
        request, 
        'stock_control/stock_detail.html', 
        {'stock': stock}
    )

@login_required
def stock_detail_modal(request, stock_id):
    stock = get_object_or_404(Stock ,id=stock_id)
    return render(
        request, 
        'stock_control/stock_list.html', 
        {'stock': stock}
    )


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
