from django.shortcuts import render
from django.views import View
from MStore.models.orderModel import Order
from django.utils.decorators import method_decorator


# Checkout class
class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer_id')
        objects =Order.get_orders_by_customer_id(customer)
        objects = objects.reverse()
        return render(request, 'order.html', {'orders': objects})
