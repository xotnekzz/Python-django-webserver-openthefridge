# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Refrigerator', '0002_auto_20170503_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='food_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
