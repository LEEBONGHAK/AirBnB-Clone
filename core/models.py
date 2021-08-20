from django.db import models
from .import managers

# Create your models here.
class TimeStampdModel(models.Model):

    """ Time Stamped Model """

    # auto_now: 값이 True일 경우 필드가 model을 save할 때 date랑 time을 기록
    # auto_now_add: 값이 True일 경우 model을 생성할 때마다 수시로 업데이트 됨
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    # 이 모델이 데이터베이스에 들어가지 않게 하기 위해서
    class Meta:
        # abstract model은 model이지만 데이터베이스에는 나타나지 않는 model
        # 대다수의 abstract model은 확장을 하려고 사용함 -> '추상' 모델
        abstract = True