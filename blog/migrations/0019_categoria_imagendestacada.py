# Generated by Django 2.2 on 2021-06-05 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210603_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagenDestacada',
            field=models.ImageField(blank=True, null=True, upload_to='imgproyectos'),
        ),
    ]