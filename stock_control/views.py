from django.shortcuts import render
from django.shortcuts import redirect
from .models import Stock
from .forms import CategoryForm

# Create your views here.
def stock_list(request):
    all_stock = Stock.objects.all()
    return render(request, 'stock_control/stock_list.html', {'all_stock': all_stock})


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