from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Product, Category
from . import forms

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

def product_add(request):
    '''product create '''
    categories = Category.objects.all()

    product_form = forms.ProductForm()
    picture_form = forms.ProductImagesForm()
    
    if request.method == "POST":
        product_form = forms.ProductForm(prefix="product", data=request.POST)
        picture_form = forms.ProductImagesForm(prefix="picture", data=request.POST, files=request.FILES)
        if product_form.is_valid() and picture_form.is_valid():
            product = product_form.save()
            picture = picture_form.save(commit=False)
            picture.product=product
            picture.save()
            return redirect(reverse('product:detail', kwargs={'product_slug':product.slug,}), status=201)
        else:
            product_form = forms.ProductForm(prefix="product")
            picture_form = forms.ProductImagesForm(prefix="picture")
        
    return render(request, 'product/create.html', locals())
    

def product_delete(request, product_slug):
    if request.method == 'POST':
        product = get_object_or_404(Product, slug=product_slug)
        product.delete()
        return redirect(reverse('product:all'))
    else:
        product = get_object_or_404(Product, slug=product_slug)
        return render(request, 'product/delete.html', locals())
        
def category_filter(request, category_slug):
    '''product detail '''
    categories = Category.objects.all()
    target_category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=target_category)
    return render(request, 'product/category.html', locals())
