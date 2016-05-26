# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('table', models.CharField(max_length=255)),
                ('primary_key', models.CharField(max_length=255)),
                ('done_by', models.CharField(max_length=255)),
                ('done_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
