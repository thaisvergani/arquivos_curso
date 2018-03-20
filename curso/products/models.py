# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)

class Product(models.Model):
    name = models.CharField(max_length=300)
    price_sell = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.ForeignKey(Category,
        null=True, on_delete=models.SET_NULL)
