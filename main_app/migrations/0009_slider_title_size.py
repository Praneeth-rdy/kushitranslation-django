# Generated by Django 3.1.5 on 2021-02-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210201_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title_size',
            field=models.IntegerField(default=44),
        ),
    ]
