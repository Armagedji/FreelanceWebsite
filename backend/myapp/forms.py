from django.forms import ModelForm
from django import forms
from .models import TodoItem
from .models import freelanceOrder

class uploadForm(ModelForm):
    title = forms.TextInput()
    completed = forms.BooleanField

    class Meta:
        model = TodoItem
        fields = ["title", "completed"]

class orderUploadForm(ModelForm):
    title = forms.TextInput()
    description = forms.TextInput()
    price = forms.IntegerField()

    class Meta:
        model = freelanceOrder
        fields = ["title", "description", "price", "completed"]