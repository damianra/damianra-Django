# Generated by Django 2.2 on 2021-05-31 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_categoria_proyecto_tag'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proyecto',
        ),
    ]
