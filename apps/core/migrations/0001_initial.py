# Generated by Django 3.2 on 2022-01-16 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=50)),
                ('app_id', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.TextField()),
                ('meeting_title', models.CharField(max_length=50)),
                ('meeting_subject', models.CharField(max_length=100)),
                ('start_time', models.TimeField(auto_now=True)),
                ('end_time', models.TimeField(auto_now_add=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
