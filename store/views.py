from django.shortcuts import render, redirect
from store.models import Product
from django.contrib.auth.decorators import login_required

from cart.cart import Cart


def home(request):
    return render(request, 'store/home.html')


def products(request):
    products = Product.objects.all()
    return render(request, 'store/products.html', {'products': products})


def about(request):
    return render(request, 'store/about.html')


def contact(request):
    return render(request, 'store/contact.html')


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('products')


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect('cart_detail')


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('cart_detail')


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('cart_detail')


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
