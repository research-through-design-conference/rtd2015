# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_2015', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=models.CharField(max_length=50, null=True, choices=[(b'home', b'Home Page'), (b'standard', b'Standard Page')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='pub_date',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
