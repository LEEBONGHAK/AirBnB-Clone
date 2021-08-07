from django_countries import countries
from django.views.generic import ListView, DetailView
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


class RoomDetail(DetailView):

    """ RoomDetail Defination """

    # 코드가 적고 많은 건 각각의 장단점이 존재함
    # object 또는 model 이름을 써도 인식됨
    # 장고는 기본적으로 DetailView를 사용하게 되면 기본적으로 url argument로 pk를 찾음
    model = models.Room


def search(request):

    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    price = request.GET.get("price", 0)
    guests = request.GET.get("guests", 0)
    bedrooms = request.GET.get("bedrooms", 0)
    beds = request.GET.get("beds", 0)
    baths = request.GET.get("baths", 0)
    s_amenities = request.GET.get("amenities")
    s_facilities = request.GET.get("facilities")
    print(s_amenities, s_facilities)

    # request에서 받은 모든 정보들
    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
        "price": price,
        "guests": guests,
        "bedrooms": bedrooms,
        "beds": beds,
        "baths": baths,
    }

    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    # 데이터베이스에서 오는 정보들
    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    return render(
        request,
        "rooms/search.html",
        context={**form, **choices},
    )
