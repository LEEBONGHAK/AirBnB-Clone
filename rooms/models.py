from django.db import models
from django_countries.fields import CountryField
from pkg_resources import parse_version
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampdModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass


# Create your models here.
# 장고나 파이썬이 보통 작동하는 방식 -> class를 가지고 string으로 만들어줌
# 장고에 있는 모든 class들이 가지고 있는 하나의 method -> __str__(string method)
class Room(core_models.TimeStampdModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    Check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # ForeignKey : model 끼리 이어주는 방법
    # 일대다 관계를 만들어 냄
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    # 다대다 관계를 가지고 있음
    roomtype = models.ManyToManyField(RoomType, blank=True)

    def __str__(self):
        return self.name