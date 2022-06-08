# Generated by Django 4.0.4 on 2022-06-08 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfirst', '0002_champion_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='lore',
            field=models.CharField(blank=True, help_text="Enter Champion's Lore", max_length=200, null=True, verbose_name='Champion Lore'),
        ),
    ]