from django.urls import path
from . import views 

app_name='product'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add/', views.product_add, name='add'),
    path('', views.product_all, name='all'),
    path('<slug:product_slug>', views.product_detail, name='detail'),
    path('<slug:product_slug>/update', views.product_update, name='update'),
    path('<slug:product_slug>/delete', views.product_delete, name='delete'),
    path('category/<slug:category_slug>', views.category_filter, name='category_filter'),
]
