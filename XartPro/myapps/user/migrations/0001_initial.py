# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-30 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='口令')),
                ('nickname', models.CharField(max_length=50, verbose_name='用户名')),
                ('photo', models.CharField(blank=True, max_length=100, null=True, verbose_name='头像')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号')),
                ('source', models.CharField(blank=True, max_length=50, null=True, verbose_name='来源')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='邮箱')),
                ('regist_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 't_user',
            },
        ),
    ]
