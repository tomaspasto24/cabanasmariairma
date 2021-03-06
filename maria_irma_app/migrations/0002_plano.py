# Generated by Django 3.0.7 on 2020-06-15 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maria_irma_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='plano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=500)),
                ('fecha', models.DateField()),
                ('imagen_link_1', models.CharField(max_length=100)),
                ('imagen_link_2', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_link_3', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_link_4', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_link_5', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_link_6', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_link_7', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_link_8', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
