from django import forms
from . import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = ('title', 'description', 'price', 'category')


class ProductImagesForm(forms.ModelForm):

    class Meta:
        model = models.ProductImage
        fields = ('description', 'image')
