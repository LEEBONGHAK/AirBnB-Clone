from os import get_terminal_size
from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.utils.html import mark_safe
from . import models

# Register your models here.
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()


# InlineModelAdmin : admin 안에 또 다른 admin을 넣는 방법
# 'TabularInline'을 사용하거나 'StackedInline'을 사용 => 보이는 방식 차이
class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
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
        "count_photos",
        "total_rating",
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

    # foreign key를 좀 더 나은 방법으로 찾을 수 있게 id로 나타냄
    # 데이터가 엄청 많을 때 유용함
    raw_id_fields = ("host",)

    # admin에서만 적용되는 save
    # def save_model(self, request, obj, form, change):
    #     print(obj, change, form)
    #     super().save_model(request, obj, form, change)

    # self : RoomAdmin / object : 현재 row
    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        # 장고 자체가 가지고 있는 보안으로 인해 입력된 값을 방지하는 것을 허용
        return mark_safe(f'<img width=50px src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
