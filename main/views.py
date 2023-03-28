from django.shortcuts import render, redirect


def home(request):
    return render(request, 'index.html')


def single_product(request, pk):
    return render(request, 'product.html')


def register(request):
    return render(request, 'register.html')


def catalog(request):
    return render(request, 'catalog.html')


def cart(request):
    return render(request, 'cart.html')

