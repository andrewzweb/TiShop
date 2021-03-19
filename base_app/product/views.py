from django.shortcuts import render


def home(request):
    greatings = 'Hello you are at home'
    return render(request, 'product/home.html', locals()) 
