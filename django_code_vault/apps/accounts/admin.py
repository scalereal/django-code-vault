from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ("email", "name", "is_admin")
    list_filter = ("is_admin",)
    fieldsets = (
        (None, {"fields": ("email", "is_staff", "is_superuser", "password")}),
        (
            "Permissions",
            {"fields": ("user_permissions",)},
        ),
    )
    add_fieldsets = (
        (
            None,
            {"fields": ("email", "is_staff", "is_superuser", "password1", "password2")},
        ),
    )
    search_fields = (
        "email",
        "name",
    )
    ordering = ("date_joined",)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
