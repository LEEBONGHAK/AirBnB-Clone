from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                # fieldset을 접었다 필 수 있는 기능
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
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
    )

    # 여러가지 것들을 기준으로 정렬할 수 있음
    ordering = ("name", "price", "bedrooms")

    list_filter = (
        "instant_book",
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
    )

    # default : icontains (insensitive 포함 => 대소문자 구분 x)
    # ^ : startswith / = : inexact 등등 많음 => 장고 문서 참조
    search_fields = (
        "=city",
        "^host__username",
    )

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    # self : RoomAdmin / object : 현재 row
    def count_amenities(self, obj):
        print(obj.amenities.all())
        return "Potato"

    count_amenities.short_description = "hello sexy!"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass