"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path

# 장고에서 settings를 import하고 싶을 때 사용
from django.conf import settings

# static파일을 제공하는 것을 도움
from django.conf.urls.static import static

# 이름 변경하면 안됨
urlpatterns = [
    path("admin/", admin.site.urls),
]


# 만약 개발중이라면 폴더안의 파일들을 제공한다.
if settings.DEBUG:
    # static을 이용해 url을 폴더에 연결시킴 -> 라우터를 생성
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)