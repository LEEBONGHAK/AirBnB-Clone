from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

# Create your models here.
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