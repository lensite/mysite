# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hosttable',
            fields=[
                ('hostid', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=50)),
                ('hostip', models.GenericIPAddressField()),
                ('hostcpu', models.CharField(max_length=50)),
                ('hostmem', models.CharField(max_length=10)),
                ('hosthdd', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='usertable',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('uname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
