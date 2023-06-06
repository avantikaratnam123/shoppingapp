from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(UserCreationForm):
  password1 = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
  password2=forms.CharField(label='confirm password(again)'),
  widget = forms.PasswordInput(attrs={'class':'form-control'})
  email = forms.CharField(required =True,widget=forms.EmailInput(attrs={'class':'form-control'}))
  class Meta:
    model = User
    fields = ['username','email','password1','password2']

    labels = {'email':'Email'}
    widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
    