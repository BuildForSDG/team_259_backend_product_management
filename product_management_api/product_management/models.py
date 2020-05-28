from django.db import models

# Create your models here.
class Producer(models.Model):

    idbusiness = models.AutoField(primary_key=True)
    producer_name = models.CharField(max_length=45)
    is_suspendend = models.PositiveSmallIntegerField()
    producer_created = models.DateTimeField(auto_now_add=True)
    producer_updated = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.producer_name

class ProductCategory(models.Model):

    idproduct_category = models.AutoField(primary_key=True)
    product_category_name = models.CharField(max_length=45,unique=True)
    product_category_added = models.DateTimeField(auto_now_add=True)
    product_category_updated = models.DateTimeField(blank=True,null=True,auto_now=True)

    def __str__(self):
        return self.product_category_name

class Product(models.Model):

    idproduct = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45,unique=True)
    quantity = models.PositiveIntegerField()
    units = models.CharField(max_length=45)
    price_per_item = models.PositiveIntegerField()
    currency = models.CharField(max_length=45)
    producers = models.ForeignKey(Producer,on_delete = models.CASCADE,related_name = 'products')
    productcategorys = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='productcat')
    product_created=models.DateTimeField(auto_now_add=True)
    product_updated=models.DateTimeField(blank=True,null=True,auto_now=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):

    idproduct_images = models.AutoField(primary_key=True)
    productimage_name = models.CharField(max_length=45)
    image = models.ImageField(upload_to='product_Images')
    products=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productimages')
    productimage_created = models.DateTimeField(auto_now_add=True)
    productimage_updated = models.DateTimeField(blank=True,null=True,auto_now=True)

    def __str__(self):
        return self.productimage_name
