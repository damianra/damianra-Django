# Generated by Django 2.2 on 2021-06-02 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210602_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
