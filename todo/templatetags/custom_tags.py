from django import template

register = template.Library()

@register.filter
def add_strings(value, arg):
    return str(arg)+str(value)