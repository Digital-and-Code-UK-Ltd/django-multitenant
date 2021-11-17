# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-12 06:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_multitenant.fields
import django_multitenant.mixins

from django_multitenant.db import migrations as tenant_migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0022_merge_20200211_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=30)),
                ('acc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenues', to='tests.Account')),
                ('project', django_multitenant.fields.TenantForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revenues', to='tests.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_multitenant.mixins.TenantModelMixin, models.Model),
        ),
        migrations.RunSQL("ALTER TABLE tests_revenue DROP CONSTRAINT tests_revenue_pkey CASCADE;", reverse_sql=''),
        tenant_migrations.Distribute('Revenue', reverse_ignore=True),
        migrations.RunSQL("ALTER TABLE tests_revenue ADD CONSTRAINT tests_revenue_pkey PRIMARY KEY (acc_id, id);", reverse_sql='')
    ]
