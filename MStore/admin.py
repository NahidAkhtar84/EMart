from django.contrib import admin
from .models.productModel import ProductModel
from .models.categoryModel import Category
from .models.customerModel import Customer
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'description', 'image', 'rating']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'password']

admin.site.register(ProductModel, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
