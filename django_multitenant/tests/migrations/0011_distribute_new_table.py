# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-17 15:14
from __future__ import unicode_literals

from django.db import migrations

from django.conf import settings

from django_multitenant.db import migrations as tenant_migrations


def get_operations():
    operations = [
        migrations.RunSQL(
            "ALTER TABLE tests_tempmodel DROP CONSTRAINT tests_tempmodel_pkey CASCADE;",
            reverse_sql="",
        ),
        migrations.RunSQL(
            "ALTER TABLE tests_tempmodel ADD CONSTRAINT tests_tempmodel_pkey PRIMARY KEY (account_id, id);",
            reverse_sql="",
        ),
    ]

    if settings.USE_CITUS:
        operations += [
            tenant_migrations.Distribute("TempModel", reverse_ignore=True),
        ]

    return operations


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0010_auto_20190517_1514"),
    ]
    operations = get_operations()
