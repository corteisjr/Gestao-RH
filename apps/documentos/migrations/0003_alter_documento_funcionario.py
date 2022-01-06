# Generated by Django 3.2 on 2022-01-06 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Funcionarios', '0001_initial'),
        ('documentos', '0002_documento_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Funcionarios.funcionario'),
            preserve_default=False,
        ),
    ]
