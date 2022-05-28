from django import forms
from .models import Signup


class UserRegistration(forms.Form):
    uemail = forms.CharField(label='uemail', max_length=50)
    upass = forms.CharField(label='upass', max_length=50)
    uname=forms.CharField(label='uname', max_length=50)
    udate=forms.CharField(label='udate', max_length=50)

class UserLogin(forms.Form):
    uemail = forms.CharField(label='uemail', max_length=50)
    upass = forms.CharField(label='upass', max_length=50)
