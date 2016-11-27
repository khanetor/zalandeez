# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zalando', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
        migrations.RemoveField(
            model_name='article',
            name='price',
        ),
        migrations.AddField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='zalando.Article'),
        ),
    ]
