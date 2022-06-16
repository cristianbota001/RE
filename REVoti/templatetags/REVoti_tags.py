from django import template

register = template.Library()



@register.filter
def list_index(listt, indexx):
    try:
        return listt[indexx]
    except IndexError:
        return ""