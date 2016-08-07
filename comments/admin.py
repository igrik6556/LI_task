# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from comments.models import CustomUser, Comment

from django.utils.translation import ugettext_lazy as _


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name',
            'last_name',
            'email',
            'birthday'
        )}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'date', 'parent')
    list_filter = ('user', )
    fieldsets = (
        (None, {'fields': ('user', 'text', 'parent')}),
        (_('Important dates'), {'fields': ('date', )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Comment, CommentAdmin)
