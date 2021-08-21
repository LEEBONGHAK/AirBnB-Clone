from django.db.models import Q
from django.shortcuts import render
from . import models

# Create your views here.
def go_conversation(request, a_pk, b_pk):

    user_one = models.User.objects.get_or_none(pk=a_pk)
    user_two = models.User.objects.get_or_none(pk=b_pk)

    if user_one is not None and user_two is not None:
        conversation = models.Conversation.objects.get(
            Q(participants=user_one) & Q(participants=user_two)
        )  # filter가 충분하지 않고, 더 복잡한 query를 다루는 방법
