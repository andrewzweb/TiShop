''' product models '''

from django.db import models
from django.utils.safestring import mark_safe
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


class ProductImage(models.Model):
    ''' product image '''
    description = models.CharField(blank=True, max_length=100)
    image = models.ImageField()
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '{}'.format(self.description)

    def small_image(self):
        return mark_safe(u'<img src="%s" width="100"/>' % self.image.url)

    small_image.short_description = 'Picture'
    small_image.allow_tags = True
