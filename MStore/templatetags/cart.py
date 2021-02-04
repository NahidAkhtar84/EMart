from django import template

register = template.Library()

@register.filter(name ='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    if str(product.id) in keys:
        return True
    return False

@register.filter(name ='cart_product_quantity')
def cart_product_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if product.id == int(id):
            return cart.get(id)
    return 0


@register.filter(name ='quantity_price_multiplication')
def quantity_price_multiplication(product, cart):
    return product.price * cart_product_quantity(product, cart)


@register.filter(name ='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += quantity_price_multiplication(p, cart)
    return sum



