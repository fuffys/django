from django.db import models
from django.core.validators import MinLengthValidator


class Lanes(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Lane Name', help_text='Enter Lane\'s Name')
    abbr = models.CharField(max_length=3, unique=True, validators=[MinLengthValidator(3)],
                            verbose_name='Lane Name Abbreviation',
                            help_text='Enter Abbreviation')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Champion(models.Model):
    TOP = 'Top lane'
    JUNGLE = 'Jungle'
    MID = 'Middle'
    ADC = 'AD Carry'
    SUPP = 'Support'

    LANES =  [
        (TOP, 'Top'),
        (JUNGLE, 'Jungle'),
        (MID, 'Middle'),
        (ADC, 'AD Carry'),
        (SUPP, 'Support')
    ]

    CLASSES = [
        ('Controller', 'Controller'),
        ('Fighter', 'Fighter'),
        ('Mage', 'Mage'),
        ('Marksman', 'Marksman'),
        ('Slayer', 'Slayer'),
        ('Tank', 'Tank'),
        ('Specialist', 'Specialist')
    ]

    RANGE_TYPE = [
        ('Melee', 'Melee'),
        ('Ranged', 'Ranged'),
        ('Hybrid', 'Hybrid')
    ]

    name = models.CharField(max_length=50, unique=True, verbose_name='Champion Name', help_text='Enter Champion\'s Name')
    lanes = models.ManyToManyField(Lanes, help_text='Choose Playable Lanes')
    champ_class = models.CharField(max_length=20, choices=CLASSES, verbose_name='Choose Class')
    range_type = models.CharField(max_length=20, choices=RANGE_TYPE, verbose_name='Choose Range Type')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


