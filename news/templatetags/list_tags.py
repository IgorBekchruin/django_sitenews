from django import template
from taggit.models import Tag

register = template.Library()


@register.simple_tag()
def get_list_tags():
    list_tags = Tag.objects.all()[:10]
    return list_tags
