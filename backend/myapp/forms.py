from django.forms import ModelForm
from django import forms
from .models import freelanceOrder


class orderUploadForm(ModelForm):
    title = forms.TextInput()
    description = forms.TextInput()
    price = forms.IntegerField()

    class Meta:
        model = freelanceOrder
        fields = ["title", "description", "price", "completed"]