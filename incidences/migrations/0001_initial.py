# Generated by Django 3.2.3 on 2021-05-31 06:14

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('risk', '0002_auto_20210530_1518'),
        ('controls', '0002_alter_control_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre del control')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Descripción del control')),
                ('date_of_occurrence', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora del suceso')),
                ('cause',
                 models.ManyToManyField(related_name='incidences', related_query_name='incidence', to='risk.Cause',
                                        verbose_name='Causas presentes')),
                ('effects',
                 models.ManyToManyField(related_name='incidences', related_query_name='incidence', to='risk.Effect',
                                        verbose_name='Consencuencias efectivas')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidences',
                                           to='risk.risk', verbose_name='Riesgo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+',
                                           to=settings.AUTH_USER_MODEL, verbose_name='Usuario registrador')),
            ],
            options={
                'verbose_name': 'Incidencia',
                'verbose_name_plural': 'Incidencias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='IncidenceControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_effective', models.BooleanField(default=False, verbose_name='Control fue efectivo?')),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidences',
                                              to='controls.control', verbose_name='Control')),
                ('incidence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='controls',
                                                to='incidences.incidence', verbose_name='Incidencia')),
            ],
        ),
    ]
