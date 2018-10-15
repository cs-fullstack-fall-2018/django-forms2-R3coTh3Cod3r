from django import forms
from .models import FormModel


class ModelofForm(forms.ModelForm):
    class Meta:
        model= FormModel
        fields = {'name', 'recipe', 'timeCook', 'dateCreated'}