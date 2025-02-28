from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def add(value, arg):
    return value + arg

@register.filter
def to_two_decimals(value):
    return Decimal(value).quantize(Decimal('0.01'))