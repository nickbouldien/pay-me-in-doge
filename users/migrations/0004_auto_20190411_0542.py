# Generated by Django 2.2 on 2019-04-11 05:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_dogecoin_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dogecoin_wallet',
            field=models.CharField(blank=True, max_length=34, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.'), django.core.validators.MinLengthValidator(34)]),
        ),
    ]