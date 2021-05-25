from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    # 장고에서 class based view는 view로 변신시켜주는 메소드가 존재
    path("", room_views.HomeView.as_view(), name="home"),
]