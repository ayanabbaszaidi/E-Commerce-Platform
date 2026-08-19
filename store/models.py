from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.name}"

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.name}"

class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
            return f"{self.name}"

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.name}"

class Stock(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
            return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
            return f"{self.name}"

