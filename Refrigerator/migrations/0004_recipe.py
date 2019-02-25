# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Refrigerator', '0003_auto_20170503_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=500)),
                ('list_id', models.CharField(max_length=500)),
            ],
        ),
    ]
