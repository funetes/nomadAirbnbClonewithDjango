from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "price", "address")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More about the space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "all_reviews",
    )
    list_filter = (
        "instant_book",
        "host__superHost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    filter_horizontal = ("amenities", "facilities", "house_rules")
    search_fields = ["^city", "^host__username"]

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
