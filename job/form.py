from .models import Applications , job
from django import forms
class Applyform(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['name' , 'email' , 'website' , 'cv' , 'coverletter']

class Jobform(forms.ModelForm):
    class Meta:
        model = job
        fields = "__all__"
        exclude = ('slug','owner',)