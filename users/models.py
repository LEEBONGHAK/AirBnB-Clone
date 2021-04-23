from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.(데이터가 보여지는 모습)
# Model에 뭘 쓰든 장고가 알아서 form을 만들어 데이터베이스에 migration과 함꼐 이 form에 필요한 정보를 요청할 것임
class User(AbstractUser):
    bio = models.TextField(default="")
