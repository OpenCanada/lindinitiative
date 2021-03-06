# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0006_add_verbose_names'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='button_external',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='button_link',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='button_text',
            field=models.CharField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='image',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='wagtailimages.Image', null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='short_description',
            field=models.CharField(max_length=256, blank=True),
        ),
    ]
