# Generated by Django 3.2.3 on 2021-05-30 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cause',
            options={'ordering': ['id'], 'verbose_name': 'Causa', 'verbose_name_plural': 'Causas'},
        ),
        migrations.AlterModelOptions(
            name='effect',
            options={'ordering': ['id'], 'verbose_name': 'Consecuencia', 'verbose_name_plural': 'Consecuencias'},
        ),
        migrations.AlterModelOptions(
            name='risk',
            options={'ordering': ['id'], 'verbose_name': 'Riesgo', 'verbose_name_plural': 'Riesgos'},
        ),
    ]