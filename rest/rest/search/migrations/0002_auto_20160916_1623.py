# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 16:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companiesbyparish',
            name='company_key',
        ),
        migrations.RemoveField(
            model_name='companiesbyparish',
            name='parish_key',
        ),
        migrations.RemoveField(
            model_name='companiesbyparish',
            name='user',
        ),
        migrations.DeleteModel(
            name='CompaniesByParish',
        ),
        migrations.DeleteModel(
            name='CompanyInfo',
        ),
        migrations.DeleteModel(
            name='Parish',
        ),
    ]