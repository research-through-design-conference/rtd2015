# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_2015', '0006_auto_20141210_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'page/%Y/%m/%d', blank=True)),
                ('home', models.ForeignKey(related_name='images', to='site_2015.Home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageImg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'page/%Y/%m/%d', blank=True)),
                ('page', models.ForeignKey(related_name='images', to='site_2015.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='img',
            name='page',
        ),
        migrations.DeleteModel(
            name='Img',
        ),
    ]
