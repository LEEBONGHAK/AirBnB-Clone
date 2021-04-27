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
        "Check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "city",
        "country",
    )

    # default : icontains (insensitive 포함 => 대소문자 구분 x)
    # ^ : startswith 등등 많음 => 장고 문서 참조
    search_fields = (
        "^city",
        "host__username",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass