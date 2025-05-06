from django import template

from django.urls import reverse

register = template.Library()

@register.simple_tag
def url_with_anchor(view_name, anchor, *args, **kwargs):
     """
     Генерирует URL для указанного view_name и добавляет якорь.
     """
     url = reverse(view_name, args=args, kwargs=kwargs)
     return f"{url}#{anchor}"