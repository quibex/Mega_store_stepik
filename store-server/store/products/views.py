from django.shortcuts import render

from products.models import Product, ProductCategory

def index(request):
    context = {
        'title': 'Mega store',
        'username': 'Elmar',
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Mega products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)