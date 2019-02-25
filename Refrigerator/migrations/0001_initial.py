# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_number', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('food_type', models.CharField(max_length=5, choices=[('육류', '육류'), ('어류', '어류'), ('과일류', '과일류'), ('야채류', '야채류'), ('유제품류', '유제품류'), ('음료류', '음료류'), ('소스류', '소스류')])),
                ('food_name', models.CharField(max_length=15)),
                ('food_purchase', models.CharField(max_length=15)),
                ('food_exdate', models.CharField(max_length=15)),
                ('food_location', models.CharField(max_length=3, choices=[('냉장', '냉장'), ('냉동', '냉동'), ('실온', '실온')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('shopping_id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('food_type', models.CharField(max_length=5, choices=[('육류', '육류'), ('어류', '어류'), ('과일류', '과일류'), ('야채류', '야채류'), ('유제품류', '유제품류'), ('음료류', '음료류'), ('소스류', '소스류')])),
                ('shopping_name', models.CharField(max_length=15)),
                ('shopping_memo', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modify_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
