from django.contrib import admin
from product_management.models import Product,Producer,ProductImage,ProductCategory
# Register your models here.
admin.site.register(Producer)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductImage)
