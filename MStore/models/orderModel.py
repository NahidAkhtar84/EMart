from django.db import models
from .customerModel import Customer
from .productModel import ProductModel
from datetime import datetime

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=15, default='')
    date = models.DateTimeField(default= datetime.now())
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer_id(customer_id):
        placed_orders = Order.objects.filter(customer = customer_id).order_by('date')
        return placed_orders