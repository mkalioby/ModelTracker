# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ModelTracker', '0002_modeltracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='new_state',
            field=jsonfield.fields.JSONField(default='{}'),
        ),
        migrations.AddField(
            model_name='history',
            name='old_state',
            field=jsonfield.fields.JSONField(default='{}'),
        ),
    ]
