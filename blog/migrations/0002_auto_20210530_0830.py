# Generated by Django 2.2 on 2021-05-30 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cursos',
            old_name='titilo',
            new_name='titulo',
        ),
    ]
