# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=20)),
                ('code_id', models.IntegerField(null=True)),
                ('type', models.IntegerField()),
                ('data1', models.IntegerField(null=True)),
                ('data2', models.IntegerField(null=True)),
                ('data3', models.IntegerField(null=True)),
                ('flag', models.BooleanField()),
                ('ans', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
