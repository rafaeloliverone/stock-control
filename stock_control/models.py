from django.db import models
from django.utils import timezone


class Stock(models.Model):
    name = models.CharField(max_length=100)
    # category = models.ForeignKey(Category)
    quantity = models.IntegerField()
    unitary_value = models.DecimalField(max_digits=5, decimal_places=2) 
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name