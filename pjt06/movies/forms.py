from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import GENRE_CHOICES, Movie 


class MovieForm(forms.ModelForm):
    genre = forms.CharField(
        max_length=30,
        widget=forms.Select(choices=GENRE_CHOICES),
    )
    release_date = forms.DateField(
        widget = forms.DateInput(
            attrs= {'type':'date'}
        )
    )
    score = forms.FloatField(
        widget = forms.NumberInput(
            attrs = {
                'min': '0',
                'max': '10',
            }
        )
    )
    class Meta:
        model = Movie
        fields = '__all__'