
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'name', 'get_is_approved_display', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('user_id', 'password')}),
        ('Personal info', {'fields': ('name',)}),
        ('Permissions', {'fields': ('is_approved', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'name', 'password1', 'password2', 'is_approved', 'is_staff', 'is_superuser'),
        }),
    )
    search_fields = ('user_id', 'name')
    ordering = ('user_id',)
    filter_horizontal = ()

    def get_is_approved_display(self, obj):
        return obj.get_is_approved_display()
    get_is_approved_display.short_description = '승인 상태'

admin.site.register(User, UserAdmin)