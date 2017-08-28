from django.contrib import admin
from .models import Actions
# Register your models here.


class ActionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)


admin.site.register(Actions, ActionsAdmin)