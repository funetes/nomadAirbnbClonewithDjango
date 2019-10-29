from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# admin.py custom admin panel looks like


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "CustomProfile",
            {
                "fields": (
                    "language",
                    "currency",
                    "superHost",
                    "bio",
                    "avatar",
                    "gender",
                    "birthDate",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superHost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superHost",
        "is_staff",
        "is_superuser",
    )
