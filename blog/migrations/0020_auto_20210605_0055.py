# Generated by Django 2.2 on 2021-06-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_categoria_imagendestacada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagenDestacada',
            field=models.FileField(blank=True, null=True, upload_to='imgproyectos'),
        ),
    ]