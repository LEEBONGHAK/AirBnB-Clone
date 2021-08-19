from django.core.exceptions import ValidationError
from django.db import models

# reverse는 url name을 필요로 하는 함수이고 그 url을 return할 것임
from django.urls import reverse
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

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "Room Types"


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    # Meta Class : 모델 내의 모든 class들 안에 있는 class / 많은 것들을 설정할 수 있다.
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "House Rules"


class Photo(core_models.TimeStampdModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    # upload_to="" : 사진이 있는 폴더 안의 어떤 폴더에다가 photo를 업로드 할 건지 말해주는 것
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

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
    guests = models.IntegerField(help_text="How many people will be staying?")
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
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    # 다대다 관계를 가지고 있음
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        for review in all_reviews:
            all_ratings += review.rating_average()
        num_reviews = len(all_reviews)
        if num_reviews == 0:
            num_reviews = 1

        return round(all_ratings / num_reviews, 2)

    def first_photo(self):

        try:
            (photo,) = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos