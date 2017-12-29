from django import template

register = template.Library()


@register.filter(name='currency')
def currency(value):
    """
    This give the '$' sign before the currency value
    """
    return '$' + str(value)
