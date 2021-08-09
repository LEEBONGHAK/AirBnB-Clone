from django import forms
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # email이나 비밀번호가 있는 field를 확인하고 싶으면 method의 이름은 clean_ 이어야 함
    # clean_ 으로 시작되는 method는 에러를 넣는 것뿐만 아니라 데이터를 정리도 해줌
    # 만약 아무것도 return 하지 않았다면 field를 지워버림
    def clean_email(self):

        email = self.cleaned_data.get("email")

        try:
            models.User.objects.get(username=email)
            return email
        except models.User.DoesNotExist:
            raise forms.ValidationError("User does not exist")

    def clean_password(self):
        pass