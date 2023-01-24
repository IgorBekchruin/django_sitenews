from django import template
from django.db.models import Count
 
from news.models import Post

register = template.Library()
 
 
@register.simple_tag
def get_popular_post():
    post = Post.objects.annotate(ncomment=Count('comments')).order_by('-ncomment')[:3]
    return post