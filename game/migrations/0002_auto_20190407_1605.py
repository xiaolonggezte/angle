# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datamodel',
            name='data1',
        ),
        migrations.RemoveField(
            model_name='datamodel',
            name='data2',
        ),
        migrations.RemoveField(
            model_name='datamodel',
            name='data3',
        ),
        migrations.AddField(
            model_name='datamodel',
            name='input',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='ans',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
