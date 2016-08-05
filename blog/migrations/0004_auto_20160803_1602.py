# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 07:02
from __future__ import unicode_literals

import blog.fields
import blog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160801_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('road', models.CharField(max_length=20)),
                ('dong', models.CharField(max_length=20)),
                ('gu', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=blog.fields.PhoneNumberField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(help_text='Markdown 문법을 써주세요.', validators=[blog.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, validators=[blog.validators.MinLengthValidator(4), blog.validators.ZipCodeValidator(True)], verbose_name='제목'),
        ),
    ]
