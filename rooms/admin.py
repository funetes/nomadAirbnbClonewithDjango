from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Amenity, models.Facility, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    # frontend에서 보여줄것들
    list_display = ("__str__", "get_thumnail")

    # 여기서 리턴되는 값을 frontend에서 사용함
    def get_thumnail(self, obj):
        return mark_safe(f"<img src={obj.file.url} width=50px />")

    # django는 value값을 안정적으로 처리한다.
    # (안정적? 사용자가 input창에 코드를 넣었을때나 등등 문제가 있는것들을 방지함,
    # 즉 앞단에서 보여질때 단순한 string이 되어버림)
    # 지금 return 되는 값이 안전하다는 판단을 내릴때 mark_safe 함수를 사용함
    get_thumnail.short_description = "thumnail"


class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = [PhotoInline]
    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "name",
                    "description",
                    "country",
                    "city",
                    "price",
                    "address",
                    "room_type",
                )
            },
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
        ("Last Details", {"fields": ("host",)}),
    )
    # 외부 admin panel
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
    # 외부 admin panel
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
    raw_id_fields = ("host",)
    filter_horizontal = ("amenities", "facilities", "house_rules")
    search_fields = ["^city", "^host__username"]

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
