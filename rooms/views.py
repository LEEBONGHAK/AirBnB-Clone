from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import render
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
        # 장고가 알아서 404 페이지를 render함
        # templatesdp 404.html을 만들고 setting에 DEBUG를 Flase로, ALLOEWD_HOSTS="*"로 설정하면 원하는 404 페이지 만들기 가능
        raise Http404()