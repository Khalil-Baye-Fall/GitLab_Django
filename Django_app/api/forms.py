from django import forms
from .models import *

class Topic_form(forms.ModelForm):
   class Meta:
       model =  Topic
       fields = '__all__'
       
    

class Lang_form(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'
    