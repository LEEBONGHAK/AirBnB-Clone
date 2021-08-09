from django.views import View  # class-based view
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.
class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")  # reverse와 같지만 View가 필요할 때 요정하는 것
    initial = {"email": "hello@world.com"}

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)


def log_out(request):
    logout(request)

    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpFrom
    success_url = reverse_lazy("core:home")  # reverse와 같지만 View가 필요할 때 요정하는 것
    initial = {
        "first_name": "BongHak",
        "last_name": "Lee",
        "email": "hello@world.com",
        "password": "123",
        "password1": "123",
    }

    def form_valid(self, form):

        # form에 문제가 없다면 유저 정보를 저장
        form.save()

        # 저장 후  해당 유저 로그인
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)