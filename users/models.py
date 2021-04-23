from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.(데이터가 보여지는 모습)
# Model에 뭘 쓰든 장고가 알아서 form을 만들어 데이터베이스에 migration과 함꼐 이 form에 필요한 정보를 요청할 것임
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )  # 튜플

    LANGAUGE_ENGLISH = "en"
    LANGAUGE_KOREA = "kr"

    LANGAUGE_CHOICES = ((LANGAUGE_ENGLISH, "English"), (LANGAUGE_KOREA, "Korean"))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    avatar = models.ImageField(blank=True)
    # null은 데이터베이스에서 사용되는 것 / blank는 form에서 사용되는 빈값
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    # CharField(max_length, default) : argumentrk가 하나만 필요 => 글자 수 제한이 있는 1줄 짜리 field
    # choices를 주어 선택하게 만들 수 도 있음 이는 form에 변화를 준 것이기 때문에 데이터베이스에 영향이 가지 않는다.
    bio = models.TextField(default="", blank=True)
    # TextField : 글자 수 제한이 없는 여러 줄을 쓸 수 있는 field
    birthdate = models.DateField(blank=True, null=True)
    langauge = models.CharField(choices=LANGAUGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)