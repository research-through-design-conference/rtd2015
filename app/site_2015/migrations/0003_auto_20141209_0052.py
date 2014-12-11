# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_2015', '0002_auto_20141207_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
