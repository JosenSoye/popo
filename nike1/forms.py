from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product,Product1,Product2

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'box','placeholder':'Enter username'}))
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'box','placeholder':'Enter first name'}))    
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'box','placeholder':'enter the email'}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'box','placeholder' : 'Enter password'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'box','placeholder': 'Confirm password'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']


class produtform(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','cat','img']

class productform1(forms.ModelForm):
    class Meta:
        model = Product1
        fields = ['name','price','cat','img']
class productform2(forms.ModelForm):
    class Meta:
        model = Product2
        fields = ['name','price','cat','img']