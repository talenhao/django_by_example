from django.contrib import admin

# Register your models here.
from .models import Post


# 定制显示
class PostAdmin(admin.ModelAdmin):
    # 定制admin界面显示的列
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    # 添加过滤功能
    list_filter = ('status', 'author', 'publish', 'created', 'updated')
    # 添加搜索功能
    search_fields = ('title', 'body')
    # 填写title后自动处理slug
    prepopulated_fields = {'slug': ("title",)}
    # 自己赶写用户id代替下拉列表，适用于用户数量相当多的情况。
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']  # 覆盖数据库的配置。

admin.site.register(Post, PostAdmin)


from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'body', 'created', 'updated', 'active')
    list_filter = ('post', 'name', 'email', 'created', 'updated', 'active')
    search_fields = ('body', 'name', 'email', 'post')
    ordering = ['post', 'active']

admin.site.register(Comment, CommentAdmin)
