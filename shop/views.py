from django.shortcuts import render

def index(request):
    return render(request, 'shop/index.html')

def product(request):
    return render(request, 'shop/product.html')

def categories(request):
    return render(request, 'shop/categories.html')

def contact(request):
    return render(request, 'shop/contact.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def cart(request):
    return render(request, 'shop/cart.html')

