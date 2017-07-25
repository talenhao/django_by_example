from django.contrib import admin

# Register your models here.
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_filter = ['title', 'slug', 'image', 'created']
    search_fields = ['created']


admin.site.register(Image, ImageAdmin)
