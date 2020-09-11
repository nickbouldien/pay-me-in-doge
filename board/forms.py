from django import forms

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
