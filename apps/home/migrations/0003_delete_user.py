# Generated by Django 3.2.6 on 2022-04-14 19:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0002_rename_siteuser_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
