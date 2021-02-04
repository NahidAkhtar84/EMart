from django.shortcuts import render, redirect
from MStore.models.customerModel import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from MStore.models.productModel import ProductModel

# Cart class
class Cart(View):
    def get(self, request):
        cart = list(request.session.get('cart').keys())
        cart_products = ProductModel.get_product_by_cartids(cart)
        return render(request, 'cart.html', {'cproducts': cart_products})

