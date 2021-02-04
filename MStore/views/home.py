from django.shortcuts import render, redirect
from django.http import  HttpResponse
from MStore.models.productModel import ProductModel
from MStore.models.categoryModel import Category
from MStore.models.customerModel import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_catrgories()
        categoryId = request.GET.get('category')

        if categoryId:
            products = ProductModel.get_all_product_byCategoryId(categoryId)
        else:
            products = ProductModel.get_all_product()
        data = {}
        data['products'] = products
        data['categories'] = categories
        return render(request, 'index.html', data)

    def post(self, request):
        productid = request.POST.get("product_id")
        remove = request.POST.get("removeitem")
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(productid)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(productid)
                    else:
                        cart[productid] = quantity - 1
                else:
                    cart[productid] = quantity + 1
            else:
                cart[productid] = 1
        else:
            cart = {}
            cart[productid] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('homepage')








