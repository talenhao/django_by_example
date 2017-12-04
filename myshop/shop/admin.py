from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['stock', 'available', 'price']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)