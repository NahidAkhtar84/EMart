from django import template

register = template.Library()

@register.filter(name ='currency_sign')
def currency_sign(currency):
    return '৳ '+str(currency)