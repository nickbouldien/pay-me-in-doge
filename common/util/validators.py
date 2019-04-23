from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


def validate_url(url):
    schemes = ("http", "https")
    validate = URLValidator(schemes)

    validate(url)
