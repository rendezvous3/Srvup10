# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 01:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=320, null=True, verbose_name='Facebook Profile Link')),
                ('twitter_handle', models.CharField(blank=True, max_length=320, null=True, verbose_name='Twitter handle')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
