from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimeStampdModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Object Definition """

    class Meta:
        verbose_name = "Room Types"
        ordering = ["created"]


class Amenity(AbstractItem):

    """ Amenity Object Definition """

    # Meta Class : 모델 내의 모든 class들 안에 있는 class / 많은 것들을 설정할 수 있다.
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rules"


class Photo(core_models.TimeStampdModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


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
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # ForeignKey : model 끼리 이어주는 방법
    # 일대다 관계를 만들어 냄
    # on_delete : 만약 User가 삭제(on_delete)되었다면 장고에게 room으로 무엇을 할건지 행동 지정 / 오직 Foreign key에만 해당
    # CASCADE : 폭포수 효과 / 제일 위에서 어떤 일이 발생하고 그것이 아래에 모든 영향을 주는 것
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    # 다대다 관계를 가지고 있음
    amenities = models.ManyToManyField("Amenity", blank=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    def __str__(self):
        return self.name