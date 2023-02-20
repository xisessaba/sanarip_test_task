# Generated by Django 3.2 on 2023-02-01 06:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Culture',
                'verbose_name_plural': 'Cultures',
            },
        ),
        migrations.CreateModel(
            name='Fermer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Fermer',
                'verbose_name_plural': 'Fermers',
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Season',
                'verbose_name_plural': 'Seasons',
            },
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contour', django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326)),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fermers.culture')),
                ('fermer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fermers.fermer')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fermers.season')),
            ],
            options={
                'verbose_name': 'Plot',
                'verbose_name_plural': 'Plots',
            },
        ),
    ]