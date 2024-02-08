# Generated by Django 5.0.1 on 2024-02-08 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_incidencia_causa_incidencia_longitud_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incidencia',
            old_name='nivel',
            new_name='zona',
        ),
        migrations.AddField(
            model_name='incidencia',
            name='demarcacion',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidencia',
            name='direccion',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidencia',
            name='inicio',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidencia',
            name='km_inicio_fin',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidencia',
            name='observaciones',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incidencia',
            name='tramo',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='longitud',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
