# Generated by Django 3.0.8 on 2020-09-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMU',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('header_secs', models.PositiveIntegerField()),
                ('orient_x', models.FloatField()),
                ('orient_y', models.FloatField()),
                ('orient_z', models.FloatField()),
                ('orient_w', models.FloatField()),
                ('angular_velocity_roll', models.FloatField()),
                ('angular_velocity_yaw', models.FloatField()),
                ('angular_velocity_pitch', models.FloatField()),
                ('linear_acceleration_forward', models.FloatField()),
                ('linear_acceleration_up', models.FloatField()),
                ('linear_acceleration_left', models.FloatField()),
            ],
        ),
    ]
