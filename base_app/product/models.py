''' product models '''

from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    ''' model product '''
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        default=0,
        max_digits=10,
        decimal_places=2,
        blank=True
     )

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
