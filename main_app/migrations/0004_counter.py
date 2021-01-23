# Generated by Django 3.1.5 on 2021-01-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210123_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=50)),
                ('duration', models.IntegerField(default=2000)),
            ],
        ),
    ]