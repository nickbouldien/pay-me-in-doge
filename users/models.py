from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from board.models import UUIDModel

dogecoin_address = RegexValidator(
    "^(D)[^OIYWa-z][A-Za-z0-9]{32}$",
    message="your dogecoin wallet address should start with the letter 'D' and be a combination of letters and numbers",
)


class Profile(UUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dogecoin_wallet = models.CharField(
        max_length=34,
        blank=True,
        null=True,
        validators=[dogecoin_address, MinLengthValidator(34)],
    )
    image = models.CharField(max_length=240, default="default.png")

    def __str__(self):
        return f"{self.user.username} Profile"
