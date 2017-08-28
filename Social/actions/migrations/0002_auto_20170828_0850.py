# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actions',
            old_name='target_ct',
            new_name='target_content_type',
        ),
    ]
