from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from . import models, forms

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


class SearchView(View):

    """ SerachView Definition """

    def get(self, request):
        # url에 어떤 것이 있는 지 확인
        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)  # django the forms API 참고

            if form.is_valid():  # form에 에러가 없으면 True를 return하는 method

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                rooms = models.Room.objects.filter(**filter_args)

                return render(
                    request,
                    "rooms/search.html",
                    context={"form": form, "rooms": rooms},
                )

        else:
            form = forms.SearchForm()

        return render(
            request,
            "rooms/search.html",
            context={"form": form},
        )
