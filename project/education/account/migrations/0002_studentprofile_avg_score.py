# Generated by Django 3.2 on 2023-05-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='avg_score',
            field=models.PositiveSmallIntegerField(default=56),
        ),
    ]