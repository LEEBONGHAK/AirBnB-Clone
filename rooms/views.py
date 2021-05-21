from datetime import datetime
from django.shortcuts import render
from . import models

# Create your views here.
# url : 요청에 바로 응답하는 방법
# view: 요청에 답을 하는 방법
def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page * page_size
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]

    # context를 이용해 template에 변수를 보낼 수 있다.
    # logic => {% if %} (파이썬 logic을 사용할 수 있게 만듬)
    # varibles => {{}}
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
