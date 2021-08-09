from django.views import View  # class-based view
from django.shortcuts import render
from . import forms

# Create your views here.
class LoginView(View):
    def get(self, request):

        form = forms.LoginForm(initial={"email": "hello@world.com"})

        return render(request, "users/login.html", {"form": form})

    def post(self, request):

        form = forms.LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)  # cleaned_data : 정리의 결과물

        return render(request, "users/login.html", {"form": form})