# Generated by Django 4.0.4 on 2022-04-28 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_alter_profile_testresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.TextField(default='Developer'),
        ),
    ]
