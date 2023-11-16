# Generated by Django 4.2.7 on 2023-11-16 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impuestos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('porcentaje', models.PositiveIntegerField()),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='UnidadMedida',
        ),
    ]