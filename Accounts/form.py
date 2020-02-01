from django import forms
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


class GirisForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20,widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError('Duzgun daxil edin')


class Qeydiyyat(forms.ModelForm):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model=User
        fields={
            'username',
            'password1',
            'password2',
        }

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parollar eyni deyil')
        return password2