# Generated by Django 2.2 on 2021-06-02 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='imagenDestacada',
            field=models.FileField(blank=True, null=True, upload_to='imgproyectos'),
        ),
    ]
