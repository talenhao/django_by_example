from django import template
from ..models import Post

from django.db.models import Count

from django.utils.safestring import mark_safe
import markdown


register = template.Library()


# tag
# 单一值
@register.simple_tag
def total_posts():
    return Post.published.count()


# 返回字典
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


# 返回一个方法
@register.assignment_tag
def get_most_comments_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


# filter
# filter: markdown
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
