# Generated by Django 4.0.4 on 2022-04-24 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_mbtitest_probability'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mbtitest',
            old_name='result',
            new_name='type',
        ),
    ]