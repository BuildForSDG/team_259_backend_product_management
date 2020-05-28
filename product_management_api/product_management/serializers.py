from rest_framework import serializers
from product_management.models import Producer,Product,ProductImage,ProductCategory
class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Producer
        fields=['url','producer_name','is_suspendend','producer_created','producer_updated']
class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ProductCategory
        fields=['url','product_category_name','product_category_added','product_category_updated']

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=Product
        fields=['url','product_name','quantity','units','price_per_item','currency',
                 'producers','productcategorys','product_created','product_updated']

class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    serializers.ImageField(use_url=True)

    class Meta:
        model=ProductImage
        fields=['url','productimage_name','image','products','productimage_created','productimage_updated']
        read_only_fields = ('productimage_created', 'productimage_updated')
