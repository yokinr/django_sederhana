from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget


class MyModelForm(forms.ModelForm):
    class Meta:
        model = ModelName
        fields = '__all__'
        widgets = {
            'field1': forms.TextInput({'class': 'form-control'}),
            # 'field2': forms.Textarea({'class': 'form-control'}),
            'field2': SummernoteWidget(),
            'field3': forms.NumberInput({'class': 'form-control'}),
        }
