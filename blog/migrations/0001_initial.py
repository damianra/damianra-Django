# Generated by Django 2.2 on 2021-05-30 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titilo', models.CharField(max_length=250)),
                ('finalizado', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250, null=True)),
                ('id_credencial', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
    ]
