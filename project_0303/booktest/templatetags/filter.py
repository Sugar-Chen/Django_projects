from django.template import Library

#创建Library对象
register = Library()


@register.filter
def mod_value(num,value):
    return num % value == 0
