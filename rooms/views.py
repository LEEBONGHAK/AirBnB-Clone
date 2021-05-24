from math import ceil
from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.
# url : 요청에 바로 응답하는 방법
# view: 요청에 답을 하는 방법
def all_rooms(request):
    page = request.GET.get("page", 1)
    # 쿼리셋만 생성할 뿐 호출하지 않는 이상 모든 요소를 즉시 불러오진 않는다.
    room_list = models.Room.objects.all()
    # 데이터 수가 페이지처럼 크지 않을 경우 이러한 것을 orphan이라고 하는데 paginator에 orphan을 정의하여 해결할 수 있음
    paginator = Paginator(room_list, 10, orphans=5)
    # get_page() : 페이지가 음수이거나 초과하면 마지막 또는 처음 페이지를 반환한다. => 핸들링할 요소가 적지만, page의 maximum, minimum을 통제하기 어렵다.
    # page() : 페이지가 음수이거나 초과하면 에러를 반환한다. => 다양하게 통제할 수 있지만 핸들링을 많이 해주어야함
    rooms = paginator.page(int(page))

    # context를 이용해 template에 변수를 보낼 수 있다.
    # logic => {% if %} (파이썬 logic을 사용할 수 있게 만듬)
    # varibles => {{}}
    return render(
        request,
        "rooms/home.html",
        context={"page": rooms},
    )
