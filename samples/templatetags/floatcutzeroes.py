from django import template
register = template.Library()

@register.filter
def floatcutzeroes(value):
    return float(value)
