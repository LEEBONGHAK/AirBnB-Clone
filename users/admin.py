from django.contrib import admin
from . import models

# Register your models here.
# admin 패널에서 User을 보고 싶어 User을 컨트롤한 클래스가 아래가 될 거야라는 의미
@admin.register(models.User)  # decorator - class바로 위에 있어야 인식 됨(줄이 띄어져 있어도 안됨)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "email", "gender", "langauge", "currency", "superhost")
    list_filter = ("superhost", "langauge", "currency")  # 하나만 있을 경우 ',' 붙여줘야함
