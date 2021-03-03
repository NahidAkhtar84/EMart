from django.contrib import admin
from .models.productModel import ProductModel
from .models.categoryModel import Category
from .models.customerModel import Customer
from .models.orderModel import Order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'brand', 'price', 'description', 'image', 'rating']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'password']

class AdminOrder(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'price', 'address', 'phone', 'date']

admin.site.register(ProductModel, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
