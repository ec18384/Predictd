# Generated by Django 4.0.4 on 2022-04-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0031_mbtimodel_headerimgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='mbtimodel',
            name='overview',
            field=models.TextField(default=''),
        ),
    ]
