import uuid
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Site(UUIDModel):
    name = models.CharField(max_length=50)
    poster = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    link = models.CharField(max_length=50)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __repr__(self):
        return "Site('{}', '{}', '{}')".format(self.name, self.link, self.id)

    def __str__(self):
        return "'{}': '{}' - '{}'".format(self.name, self.link, self.description)

