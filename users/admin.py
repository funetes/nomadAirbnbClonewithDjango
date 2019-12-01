from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models

# from rooms.models import Room

# admin.py custom admin panel looks like


# class RoomInline(admin.TabularInline):
#     model = Room


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # inlines = [RoomInline]
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
