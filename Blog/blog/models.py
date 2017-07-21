# django.db.models.Model
from django.db import models

# Create your models here.
from unidecode import unidecode
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# 经典url
from django.core.urlresolvers import reverse


# 自定义管理器
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


# posts
class Post(models.Model):
    """
    文章提交表
    """
    # 自定义manager
    objects = models.Manager()  # default manager.
    published = PublishedManager()  # our custom manager.
    # models
    STATUS_CHOICES = (
        ('draft', "Draft"),  # 草稿
        ('published', 'Published'),  # 发布
    )
    title = models.CharField(max_length=250)  # 标题
    slug = models.SlugField(  # allow_unicode=True, 1.9版本开始支持。
                            max_length=250,  # slug：短标题
                            unique_for_date='publish', )  # publish字段日期惟一

    author = models.ForeignKey(User,   # 外键：User
                               related_name='blog_posts')
    body = models.TextField()
    # "pytz" module is required by SQLite.
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    tags = TaggableManager()

    # canonical URLs for models
    def get_absolute_url(self):
        # slug使用unicode
        self.slug = unidecode(self.slug)
        return reverse('blog:post_detail',
                       args=[
                           self.publish.year,
                           self.publish.strftime('%m'),
                           self.publish.strftime('%d'),
                           self.slug
                       ])

    class Meta:
        db_table = 'blog_post_table'
        ordering = ('-publish', '-status') # 排序方式：先按倒序发布，再按倒序状态

    def __str__(self):
        """
        The __unicode__() method is obsolete in python3.x.
        :return:
        """
        return self.title


# comments
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Mata:
        ordering = ('created',)

    def __str__(self):
        return "Comment by {} on {}.".format(self.name, self.post)
