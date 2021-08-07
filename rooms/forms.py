from django import forms
from django.forms.forms import Form
from . import models


class SearchForm(forms.Form):

    """ Form for search.html """

    city = forms.CharField(initial="Aywhere")
    price = forms.IntegerField(required=False)
    room_type = forms.ModelChoiceField(queryset=models.RoomType.objects.all())