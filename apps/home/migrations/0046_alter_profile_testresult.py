# Generated by Django 4.0.4 on 2022-04-27 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0045_alter_profile_testresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='testResult',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.mbtitest'),
        ),
    ]