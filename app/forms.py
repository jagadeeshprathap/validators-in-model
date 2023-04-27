from django import forms
from app.models import *

class topicform(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class webpageform(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'