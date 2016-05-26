# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelTracker', '0002_modeltracker'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('modeltracker_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ModelTracker.ModelTracker')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
            bases=('ModelTracker.modeltracker',),
        ),
    ]
