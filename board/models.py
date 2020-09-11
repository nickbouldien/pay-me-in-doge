import uuid
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from vote.models import VoteModel
from common.util.validators import validate_url


# TODO - move this class out of here
class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Site(VoteModel, models.Model):
    name = models.CharField(max_length=50)
    poster = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    url = models.CharField(max_length=50, validators=[validate_url])
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return "Site( id - {}, '{}', '{}')".format(self.id, self.name, self.url)

    def __str__(self):
        return "'{}': '{}' - '{}'".format(self.name, self.url, self.description)

    def get_absolute_url(self):
        return reverse("site-detail", kwargs={"pk": self.pk})

