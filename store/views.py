from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Category, Product


def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', {'products': products})





def category_list(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})
