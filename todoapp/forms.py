from django.forms import ModelForm
from django import forms
from .models import Todolist

class CreateTodoForm(forms.ModelForm):
    name = forms.CharField(label = "Todo", max_length=100)
    complete = forms.BooleanField(required=False)

    class Meta:
        model = Todolist
        fields = ['name', 'complete',]