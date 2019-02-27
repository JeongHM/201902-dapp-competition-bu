# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-25 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receive_Google_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key1', models.IntegerField(default=0)),
                ('G_Word', models.CharField(max_length=200)),
                ('G_Rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Receive_Naver_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key1', models.IntegerField(default=0)),
                ('N_Word', models.CharField(max_length=200)),
                ('N_Rating', models.IntegerField(default=0)),
            ],
        ),
    ]