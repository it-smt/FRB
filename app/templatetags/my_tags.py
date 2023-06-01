from django import template

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    return f'{value[:arg]}'


@register.filter(name='my_len')
def my_len(value):
    return len(value)


@register.filter(name='get_list')
def get_list(value, arg):
    return value.split('\r\n')[arg]
