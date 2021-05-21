from math import ceil
from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.
# url : 요청에 바로 응답하는 방법
# view: 요청에 답을 하는 방법
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page * page_size
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = ceil(models.Room.objects.count() / page_size)

    # context를 이용해 template에 변수를 보낼 수 있다.
    # logic => {% if %} (파이썬 logic을 사용할 수 있게 만듬)
    # varibles => {{}}
    return render(
        request,
        "rooms/home.html",
        context={
            "rooms": all_rooms,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count + 1),
        },
    )
