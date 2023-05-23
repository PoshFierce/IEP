# Generated by Django 3.2 on 2023-05-21 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='avg_score',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CourseUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(default=2023)),
                ('students_count', models.PositiveSmallIntegerField(default=0)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.course')),
            ],
        ),
    ]
