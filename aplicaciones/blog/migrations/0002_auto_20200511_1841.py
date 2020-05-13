# Generated by Django 3.0.6 on 2020-05-11 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='eliminado',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='eliminado',
        ),
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]