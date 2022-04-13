# Generated by Django 4.0.4 on 2022-04-13 16:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lanes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter Lane's Name", max_length=50, unique=True, verbose_name='Lane Name')),
                ('abbr', models.CharField(help_text='Enter Abbreviation', max_length=3, unique=True, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='Lane Name Abbreviation')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter Champion's Name", max_length=50, unique=True, verbose_name='Champion Name')),
                ('champ_class', models.CharField(choices=[('Controller', 'Controller'), ('Fighter', 'Fighter'), ('Mage', 'Mage'), ('Marksman', 'Marksman'), ('Slayer', 'Slayer'), ('Tank', 'Tank'), ('Specialist', 'Specialist')], max_length=20, verbose_name='Choose Class')),
                ('range_type', models.CharField(choices=[('Melee', 'Melee'), ('Ranged', 'Ranged'), ('Hybrid', 'Hybrid')], max_length=20, verbose_name='Choose Range Type')),
                ('lanes', models.ManyToManyField(help_text='Choose Playable Lanes', to='myfirst.lanes')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]