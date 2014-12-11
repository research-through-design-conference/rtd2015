# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_2015', '0007_auto_20141210_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='published',
        ),
    ]
