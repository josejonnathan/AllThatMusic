from django.contrib import admin
from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff']
    list_editable = ['is_staff']
    search_fields = ['username', 'email']
    
@admin.register(models.UserCollection)
class UserCollectionAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user']
    filter_horizontal = ['albums', 'songs', 'artists']