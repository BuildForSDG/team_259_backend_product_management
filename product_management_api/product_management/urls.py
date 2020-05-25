from django.urls import include, path
from rest_framework import routers
from product_management.views import (ProductViewSet,ProducerViewSet,ProductImageViewSet,ProductCategoryViewSet)
router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'producer', ProducerViewSet)
router.register(r'product_category',ProductCategoryViewSet)
router.register(r'product_image',ProductImageViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
