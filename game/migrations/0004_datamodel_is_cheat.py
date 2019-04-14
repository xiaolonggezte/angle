# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_datamodel_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='datamodel',
            name='is_cheat',
            field=models.BooleanField(default=False),
        ),
    ]
