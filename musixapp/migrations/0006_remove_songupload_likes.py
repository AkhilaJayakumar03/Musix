# Generated by Django 4.1.5 on 2023-07-17 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musixapp', '0005_delete_profileimage_songupload_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songupload',
            name='likes',
        ),
    ]
