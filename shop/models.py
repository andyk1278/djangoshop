from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])

class Product(models.Model):
    # many-to-one relationship: product belongs to one category - category contains many products
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    # name of product
    name = models.CharField(max_length=200, db_index=True)
    # slug for product for use in URL
    slug = models.SlugField(max_length=200, db_index=True)
    # optional image of product
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    # optional description of product
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # boolean to indicate whether product is available or not
    available = models.BooleanField(default=True)
    # stores when object was created
    created = models.DateTimeField(auto_now_add=True)
    # stores when object was updated
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
