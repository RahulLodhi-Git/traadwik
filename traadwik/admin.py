from django.contrib import admin
from .models import Brand, ProductCategory, PriceList, Jobs, product

# Register your models here.
admin.site.register(Brand)
admin.site.register(ProductCategory)
admin.site.register(PriceList)
admin.site.register(Jobs)
admin.site.register(product)