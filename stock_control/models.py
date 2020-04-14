from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL
    )
    quantity = models.IntegerField()
    unitary_value = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        ordering=['id']

    def __str__(self):
        return self.name
