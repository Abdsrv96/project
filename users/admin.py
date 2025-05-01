from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from users.forms import RegisterForm, EditUserForm

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    edit_form = EditUserForm
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_banned')
    search_fields = ('email', 'first_name', 'last_name')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')
        }),
    )

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_banned', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
