# Generated by Django 4.2.7 on 2023-11-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_productos_existencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='codigo_barra',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='codigo_producto',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]