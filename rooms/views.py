from math import ceil
from datetime import datetime
from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.
# url : 요청에 바로 응답하는 방법
# view: 요청에 답을 하는 방법
def all_rooms(request):
    page = request.GET.get("page")
    # 쿼리셋만 생성할 뿐 호출하지 않는 이상 모든 요소를 즉시 불러오진 않는다.
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)

    # context를 이용해 template에 변수를 보낼 수 있다.
    # logic => {% if %} (파이썬 logic을 사용할 수 있게 만듬)
    # varibles => {{}}
    return render(
        request,
        "rooms/home.html",
        context={"rooms": rooms},
    )
