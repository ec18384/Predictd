# Generated by Django 4.0.4 on 2022-04-25 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_mbtitest_fvst_mbtitest_ivse_mbtitest_ivss_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='mbti_nickname',
        ),
        migrations.AddField(
            model_name='mbtitest',
            name='nickname',
            field=models.TextField(default=''),
        ),
    ]