# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('slug', models.CharField(max_length=256, db_index=True, verbose_name='网址')),
                ('content', models.TextField(default='', verbose_name='内容', blank=True)),
                ('published', models.BooleanField(default=True, verbose_name='正式发布')),
                ('author', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True, verbose_name='作者')),
            ],
            options={
                'verbose_name': '教程',
                'verbose_name_plural': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='栏目名称')),
                ('slug', models.CharField(max_length=256, db_index=True, verbose_name='栏目网址')),
                ('intro', models.TextField(verbose_name='栏目简介', default='')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '栏目',
                'verbose_name_plural': '栏目',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ManyToManyField(verbose_name='归属栏目', to='shows.Column'),
        ),
    ]
