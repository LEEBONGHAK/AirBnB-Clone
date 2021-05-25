from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import render, redirect
from . import models

# Create your views here.
# url : 요청에 바로 응답하는 방법
# view: 요청에 답을 하는 방법
class HomeView(ListView):

    """ HomeView Defination """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(
            request,
            "rooms/detail.html",
            context={"room": room},
        )
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))