# -*- coding: utf-8 -*-

"""
Simplified json encoder filter for react_django_filters.

Example:
    {{ my_dict|react_json }}
"""

from __future__ import unicode_literals
import json
from django.utils.safestring import mark_safe
import django
from django import template

if django.VERSION >= (1, 10):
    from django.core.serializers.json import DjangoJSONEncoder
else:
    from django_react_filters.serializers import DjangoJSONEncoder

register = template.Library()


@register.filter('react_json')
def json_filter(value):
    return mark_safe(json.dumps(value, cls=DjangoJSONEncoder))
