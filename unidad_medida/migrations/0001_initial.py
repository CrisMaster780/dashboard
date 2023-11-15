# Generated by Django 4.2.7 on 2023-11-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=250)),
                ('resumido', models.CharField(max_length=10)),
                ('estado', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
    ]
