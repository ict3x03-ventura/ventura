from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User
from base.models import Users as baseModel
'''
form that uses built in user creation form
'''
class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=50, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
    
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
    
'''
Basic model form that uses the Users model, extended from auth Model
'''
class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=50, required=True,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = baseModel
        fields = ('phone_number', 'email')
        