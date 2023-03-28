from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='index'),
    path('product/<int:pk>/', single_product, name='product'),
    path('catalog/', catalog, name='catalog'),
    path('register/', register, name='register'),
    path('cart/', cart, name='cart'),
]
