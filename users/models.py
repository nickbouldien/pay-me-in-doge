from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from board.models import UUIDModel

# from PIL import Image

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
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    # def get_absolute_url(self):
    #     print("self: ", self.id, self.pk)
    #     return reverse("public-profile", kwargs={"pk": self.id})
