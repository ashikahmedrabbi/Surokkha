from django import forms
from .models import vaccines
from .models import Review

class vaccinesForm(forms.ModelForm):
    class Meta: 
        model = vaccines
        fields = '__all__'

class reviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name',  'comment']