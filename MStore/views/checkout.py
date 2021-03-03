from django.shortcuts import render, redirect
from django.views import View
from MStore.models.productModel import ProductModel
from MStore.models.customerModel import Customer
from MStore.models.orderModel import Order


# Checkout class
class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cproduct = request.session.get('cart')
        print('cart:', cproduct)
        products = ProductModel.get_product_by_cartids(list(cproduct.keys()))
        for p in products:
            orders = Order(
                customer=Customer(id=customer),
                product=p,
                quantity=cproduct.get(str(p.id)),
                price=p.price,
                address=address,
                phone=phone
            )
            orders.placeOrder()
        request.session['cart'] = {}
        return redirect('cart')
