# Generated by Django 3.0.8 on 2020-08-27 16:41

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lidar3D',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=list, null=True)),
                ('is_bigendian', models.BooleanField()),
                ('point_step', models.IntegerField()),
                ('row_step', models.IntegerField()),
                ('data', models.BinaryField()),
                ('is_dense', models.BooleanField()),
            ],
        ),
    ]