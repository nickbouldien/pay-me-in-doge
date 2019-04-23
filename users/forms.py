from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    dogecoin_wallet = forms.CharField(
        min_length=34,
        validators=[
            RegexValidator(
                "^(D)[^OIYWa-z][A-Za-z0-9]{32}$",
                message="your dogecoin wallet address should start with the letter 'D' and be a combination of letters and numbers",
            )
        ],
    )

    class Meta:
        model = Profile
        fields = ["dogecoin_wallet", "image"]
