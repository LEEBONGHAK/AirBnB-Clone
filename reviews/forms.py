from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    accuracy = forms.ImageField(max_value=5, min_value=1)
    communication = forms.ImageField(max_value=5, min_value=1)
    cleanlines = forms.ImageField(max_value=5, min_value=1)
    location = forms.ImageField(max_value=5, min_value=1)
    check_in = forms.ImageField(max_value=5, min_value=1)
    value = forms.ImageField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "review",
            "accuracy",
            "communication",
            "cleanlines",
            "location",
            "check_in",
            "value",
        )

    def save(self):

        review = super().save(commit=False)
        return review