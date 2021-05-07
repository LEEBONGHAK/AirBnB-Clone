from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms__models


class RoomInline(admin.TabularInline):

    model = rooms__models.Room


# Register your models here.
# admin 패널에서 User을 보고 싶어 User을 컨트롤한 클래스가 아래가 될 거야라는 의미
@admin.register(models.User)  # decorator - class바로 위에 있어야 인식 됨(줄이 띄어져 있어도 안됨)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "langauge",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "langauge",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
