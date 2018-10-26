from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product.html/', views.product, name='product'),
    path('contact.html/', views.contact, name='contact'),
    path('checkout.html/', views.checkout, name='checkout'),
    path('categories.html/', views.categories, name='categories'),
    path('cart.html/', views.cart, name='cart'),
    ]