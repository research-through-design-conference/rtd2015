# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_2015', '0004_auto_20141209_0057'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='nav_text',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
