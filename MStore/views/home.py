from django.shortcuts import render, redirect
from django.http import  HttpResponse
from MStore.models.productModel import ProductModel
from MStore.models.categoryModel import Category
from MStore.models.customerModel import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


# Create your views here.
def index(request):
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








