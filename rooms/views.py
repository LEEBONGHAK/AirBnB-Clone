from django.views.generic import ListView, DetailView
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


class RoomDetail(DetailView):

    """ RoomDetail Defination """

    # 코드가 적고 많은 건 각각의 장단점이 존재함
    # object 또는 model 이름을 써도 인식됨
    # 장고는 기본적으로 DetailView를 사용하게 되면 기본적으로 url argument로 pk를 찾음
    model = models.Room