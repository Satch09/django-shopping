from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=120)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(
        max_digits=5, decimal_places=2, null=False)
    product_summary = models.TextField(default="this is cool")
    featured = models.BooleanField()

    def __str__(self):
        return self.product_name
