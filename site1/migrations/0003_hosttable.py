# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0002_auto_20170706_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='hosttable',
            fields=[
                ('hostid', models.AutoField(primary_key=True, serialize=False)),
                ('hostname', models.CharField(max_length=20)),
                ('hostcpu', models.CharField(max_length=20)),
                ('hostmem', models.CharField(max_length=20)),
                ('hostcpuhdd', models.CharField(max_length=20)),
            ],
        ),
    ]
