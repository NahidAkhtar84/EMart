from django import template

register = template.Library()

@register.filter(name ='currency_sign')
def currency_sign(currency):
    return '৳ '+str(currency)


@register.filter(name ='multiply_orders_product_quantity')
def multiply_orders_product_quantity(productprice, quantity):
    return productprice * quantity