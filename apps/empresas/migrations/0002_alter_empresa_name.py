# Generated by Django 3.2 on 2022-01-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
