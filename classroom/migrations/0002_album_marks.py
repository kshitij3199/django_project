# Generated by Django 2.0 on 2017-12-20 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]