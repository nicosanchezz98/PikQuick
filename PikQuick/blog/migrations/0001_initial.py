# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha')),
                ('content', models.TextField(max_length=150, verbose_name=b'content')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desscription', models.CharField(max_length=150, verbose_name=b'description')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name=b'fecha')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=15, verbose_name=b'id')),
                ('mail', models.CharField(max_length=30, verbose_name=b'mail')),
                ('password', models.CharField(max_length=10, verbose_name=b'password')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='blog.User'),
        ),
        migrations.AddField(
            model_name='coment',
            name='user',
            field=models.ForeignKey(to='blog.User'),
        ),
    ]
