from django import forms
from django.contrib.auth.models import User
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )

    # email이나 비밀번호가 있는 field를 확인하고 싶으면 method의 이름은 clean_ 이어야 함
    # clean 으로 시작되는 method는 에러를 넣는 것뿐만 아니라 데이터를 정리도 해줌
    # 만약 아무것도 return 하지 않았다면 field를 지워버림
    def clean(self):

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("passwords")

        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong")
                )  # 특정 field에 작접 에러를 추가하기 위해
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )  # password 확인

    def clean_email(self):  # 중복 email 확인
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError(
                "That email is already taken", code="existing_user"
            )
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):  # password 확인
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")

        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(
            commit=False
        )  # commit=False : object를 생성하지만 DB에는 올리지 말라는 의미

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user.username = email
        user.set_password(password)

        user.save()
