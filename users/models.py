import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags  # html 제외한 text 형태를 제외한 형태로 return
from django.template.loader import render_to_string  # template을 load해서 render하는 것
from django.shortcuts import reverse


# Create your models here.(데이터가 보여지는 모습)
# Model에 뭘 쓰든 장고가 알아서 form을 만들어 데이터베이스에 migration과 함꼐 이 form에 필요한 정보를 요청할 것임
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )  # 튜플

    LANGAUGE_ENGLISH = "en"
    LANGAUGE_KOREA = "kr"

    LANGAUGE_CHOICES = ((LANGAUGE_ENGLISH, _("English")), (LANGAUGE_KOREA, _("Korean")))

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = ((CURRENCY_USD, "USD"), (CURRENCY_KRW, "KRW"))

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    # null은 데이터베이스에서 사용되는 것 / blank는 form에서 사용되는 빈값
    gender = models.CharField(
        _("gender"), choices=GENDER_CHOICES, max_length=10, blank=True
    )
    # CharField(max_length, default) : argumentrk가 하나만 필요 => 글자 수 제한이 있는 1줄 짜리 field
    # choices를 주어 선택하게 만들 수 도 있음 이는 form에 변화를 준 것이기 때문에 데이터베이스에 영향이 가지 않는다.
    bio = models.TextField(_("bio"), default="", blank=True)
    # TextField : 글자 수 제한이 없는 여러 줄을 쓸 수 있는 field
    birthdate = models.DateField(blank=True, null=True)
    langauge = models.CharField(
        _("language"),
        choices=LANGAUGE_CHOICES,
        max_length=2,
        blank=True,
        default=LANGAUGE_KOREA,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_KRW
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=120, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    def get_absolute_url(self):
        return reverse(
            "users:profile", kwargs={"pk": self.pk}
        )  # Detail안에 있는 모델을 보기 위해 url return / reverse는 url과 user profile을 반대로 해줄 것임 / admin에서 웹사이틀 무엇인가를 보고 싶다면 쓰기 좋음

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                _("Verify Airbnb Account"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=True,
                html_message=html_message,
            )
            self.save()

        return