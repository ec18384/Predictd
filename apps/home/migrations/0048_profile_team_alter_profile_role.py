# Generated by Django 4.0.4 on 2022-04-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0047_alter_profile_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='team',
            field=models.TextField(default='App Development'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.TextField(default='Software Engineer'),
        ),
    ]
