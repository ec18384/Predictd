# Generated by Django 4.0.4 on 2022-04-27 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_alter_profile_mbti_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mbti_type',
        ),
        migrations.AddField(
            model_name='profile',
            name='mbti_result',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.mbtitest'),
        ),
    ]
