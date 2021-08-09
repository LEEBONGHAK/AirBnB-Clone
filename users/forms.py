from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # email이나 비밀번호가 있는 field를 확인하고 싶으면 method의 이름은 clean_ 이어야 함
    # clean 으로 시작되는 method는 에러를 넣는 것뿐만 아니라 데이터를 정리도 해줌
    # 만약 아무것도 return 하지 않았다면 field를 지워버림
    def clean(self):

        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

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
