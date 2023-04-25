from django.urls import path
from shop.views import *

urlpatterns = [
    path('/add_product/', add_product, name='add_product'),
    path('/products/', products, name='products'),
    path('/product_detail/', product_detail, name='product_detail'),
    path('/products_customer/', products_customer, name='products_customer'),
]
