# Generated by Django 2.2 on 2021-06-03 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_contacto_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
