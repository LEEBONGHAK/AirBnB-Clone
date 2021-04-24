from django.db import models

# Create your models here.


class TimeStampdModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    # 이 모델이 데이터베이스에 들어가지 않게 하기 위해서
    class Meta:
        # abstract model은 model이지만 데이터베이스에는 나타나지 않는 model
        # 대다수의 abstract model은 확장을 하려고 사용함 -> '추상' 모델
        abstract = True