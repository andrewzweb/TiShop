''' admin product '''

from django.contrib import admin
from . import models


class ProductImagesInstanceInline(admin.TabularInline):
    model = models.ProductImage
    fields = ('small_image', 'description', 'image')
    readonly_fields = ('small_image',)
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    ''' product admin '''
    inlines = (ProductImagesInstanceInline,)
    list_display = (
        'view_name_and_price',
        'title',
        'price',
        'category',
        'updated',
        'created')
    list_editable = ('title', 'price')
    search_fields = ('title', 'description')
    list_filter = ('category', 'updated', 'created')

    def view_name_and_price(self, obj):
        ''' view name and price in one field '''
        return "Item: {}  Price: {} usd".format(obj.title, obj.price)


@admin.register(models.ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    ''' product image '''
    list_display = ('description','small_image')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ''' category '''
    list_display = ('title',)
