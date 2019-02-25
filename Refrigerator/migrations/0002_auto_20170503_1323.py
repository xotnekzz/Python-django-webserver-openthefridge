# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Refrigerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_image',
            field=models.ImageField('Uploaded food_image',blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_location',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='food',
            name='food_type',
            field=models.CharField(max_length=10),
        ),
    ]
