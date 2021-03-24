from django.urls import path
from . import views 

app_name='product'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_all, name='all'),
    path('<slug:product_slug>', views.product_detail, name='detail'),
    path('category/<slug:category_slug>', views.category_filter, name='category_filter'),
]
