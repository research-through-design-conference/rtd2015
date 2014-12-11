# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_2015', '0003_auto_20141209_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='top_level_nav',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
