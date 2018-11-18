from .models import Account
from django.contrib.auth.models import User
from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
