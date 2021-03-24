from django.shortcuts import render, get_object_or_404

from .models import Product, Category

def home(request):
    ''' home '''
    greatings = 'Hello you are at home'
    return render(request, 'product/home.html', locals())

def product_all(request):
    ''' product all '''
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'product/list.html', locals())

def product_detail(request, product_slug):
    '''product detail '''
    categories = Category.objects.all()
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product/detail.html', locals())

def category_filter(request, category_slug):
    '''product detail '''
    categories = Category.objects.all()
    target_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=target_category)
    return render(request, 'product/category.html', locals())
