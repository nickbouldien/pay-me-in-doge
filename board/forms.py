from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import Site

from common.util.validators import validate_url


class SiteUpdateForm(forms.ModelForm):
    url = forms.CharField(validators=[validate_url])

    class Meta:
        model = Site
        fields = ["name", "url", "description"]


class SiteCreateForm(forms.ModelForm):
    url = forms.CharField(validators=[validate_url])

    class Meta:
        model = Site
        fields = ["name", "url", "description"]

