from django.contrib import admin
from .models import Brand, Size, Product, Category, Gender, Stock

# Register your models here.

admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Stock)
