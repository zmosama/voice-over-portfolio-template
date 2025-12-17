from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from unfold.admin import ModelAdmin
from .models import VoiceOver

# Unfold-styled User Admin
admin.site.unregister(User)
@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass

@admin.register(VoiceOver)
class VoiceOverAdmin(ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
