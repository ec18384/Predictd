# Generated by Django 3.2.6 on 2022-04-14 19:20

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='auth.user')),
                ('MBTI_Type', models.CharField(default='XXXX', max_length=4)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
