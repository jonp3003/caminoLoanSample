from django.db import models

# Create your models here.

BTYPE =   (
                ('', 'Select One'),
                ('fdt', 'Food Truck'),
                ('cst', 'Construction'),
                ('res', 'Restaurant'),
                ('bar', 'Barbershop'),
                ('oth', 'Other')
            )

class Product(models.Model):

    name        = models.CharField(max_length=50)
    amount      = models.DecimalField(max_digits=20, decimal_places=2)
    type        = models.CharField(max_length=3, choices=BTYPE)
    years       = models.IntegerField()
