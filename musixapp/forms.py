
from django import forms



class songuploadform(forms.Form):
    filmname=forms.CharField(max_length=250)
    musicname=forms.CharField(max_length=250)
    image=forms.FileField()
    singers=forms.CharField(max_length=250)
    language=forms.CharField(max_length=250)
    audio=forms.FileField()