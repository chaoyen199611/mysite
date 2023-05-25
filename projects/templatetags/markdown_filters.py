from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter
@stringfilter
def markdown_tags(value):
    return mark_safe(markdown.markdown(value, extensions=['extra','codehilite']))
