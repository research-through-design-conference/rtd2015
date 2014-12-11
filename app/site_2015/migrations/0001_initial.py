# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'page/%Y/%m/%d', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=255, unique=True, null=True)),
                ('text', models.TextField()),
                ('header_image', models.FileField(null=True, upload_to=b'page/%Y/%m/%d', blank=True)),
                ('pub_date', models.DateTimeField()),
                ('published', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='img',
            name='page',
            field=models.ForeignKey(related_name='images', to='site_2015.Page'),
            preserve_default=True,
        ),
    ]
