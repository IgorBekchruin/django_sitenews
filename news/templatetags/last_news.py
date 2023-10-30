from django import template

from news.models import Post

register = template.Library()


@register.simple_tag()
def get_last_post():
    last_post = Post.objects.order_by("-created_at")[0:2]
    return last_post
