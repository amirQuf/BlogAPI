# Generated by Django 3.1 on 2021-05-01 09:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_auto_20210501_0902'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Save_messages',
            new_name='SavePost',
        ),
    ]