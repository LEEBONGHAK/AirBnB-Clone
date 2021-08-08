from django.views import View  # class-based view
from django.shortcuts import render

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        pass