from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import persona


BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'))


class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(required=False,
                widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
    persona = forms.ModelMultipleChoiceField(required=True,queryset=persona.objects.all(),
            widget=forms.CheckboxSelectMultiple())

class personaForm(forms.ModelForm):
        class Meta:
                model = persona
                fields = ['nombre','apellidos','foto','archivo']
