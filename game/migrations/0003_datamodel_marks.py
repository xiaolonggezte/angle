# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190407_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodel',
            name='marks',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
