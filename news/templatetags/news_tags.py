from django import template

from ..models import Turi,Gul

register = template.Library()

@register.simple_tag
def all_tur():
    return Turi.objects.all()

@register.simple_tag
def all_gul():
    return Gul.objects.all()