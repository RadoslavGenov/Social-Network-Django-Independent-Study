# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20170324_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(default=0, db_index=True),
        ),
    ]
