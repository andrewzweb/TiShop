from django.shortcuts import render, get_object_or_404

from .models import Product

def home(request):
    ''' home '''
    greatings = 'Hello you are at home'
    return render(request, 'product/home.html', locals())

def product_all(request):
    ''' product all '''
    products = Product.objects.all()
    return render(request, 'product/list.html', locals())

def product_detail(request, product_slug):
    '''product detail '''
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product/detail.html', locals())
