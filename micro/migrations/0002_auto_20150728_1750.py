# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0001_squashed_0003_auto_20150722_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microsection',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='microsection',
            name='heading',
            field=models.CharField(max_length=512, blank=True),
        ),
    ]
