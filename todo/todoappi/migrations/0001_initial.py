# Generated by Django 3.0.5 on 2020-04-08 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', models.TextField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
