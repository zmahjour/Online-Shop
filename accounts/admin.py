from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Address


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["full_name", "phone_number", "is_staff"]
    list_filter = ["is_staff"]
    fieldsets = [
        (None, {"fields": ["full_name", "phone_number", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_staff"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "fields": ["phone_number", "full_name", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["full_name", "phone_number"]
    ordering = ["full_name"]
    filter_horizontal = []


admin.site.register(Address)
