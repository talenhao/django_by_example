from django.contrib import admin

# Register your models here.
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_filter = ['title', 'slug', 'image', 'created', "total_likes"]
    list_display = ("title", 'slug', 'image', 'created', "total_likes")
    search_fields = ['created']


admin.site.register(Image, ImageAdmin)
