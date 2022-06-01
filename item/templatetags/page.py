from django import template

register = template.Library()

@register.filter(name='add')
def add(a, b):
    return(a+b)

@register.filter(name='sub')
def sub(a, b):
    return(a-b)
