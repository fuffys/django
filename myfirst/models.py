from django.db import models
from django.core.validators import MinLengthValidator
def poster_path(instance, filename):
    return "myfirst/images/" + str(instance.name) + "/poster/" + filename


class Lanes(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Lane Name', help_text='Enter Lane\'s Name')
    abbr = models.CharField(max_length=3, unique=True, validators=[MinLengthValidator(3)],
                            verbose_name='Lane Name Abbreviation',
                            help_text='Enter Abbreviation')

    def __str__(self):
        return self.name


class Legacy(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Legacy Name', help_text='Enter Legacy\'s Name')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Champion(models.Model):

    CLASSES = [
        ('Controller', 'Controller'),
        ('Enchanter', 'Enchanter'),
        ('Catcher', 'Catcher'),
        ('Fighter', 'Fighter'),
        ('Juggernaut', 'Juggernaut'),
        ('Diver', 'Diver'),
        ('Mage', 'Mage'),
        ('Burst', 'Burst'),
        ('Battlemage', 'Battlemage'),
        ('Artillery', 'Artillery'),
        ('Marksman', 'Marksman'),
        ('Slayer', 'Slayer'),
        ('Assassin', 'Assassin'),
        ('Skirmisher', 'Skirmisher'),
        ('Tank', 'Tank'),
        ('Vanguard', 'Vanguard'),
        ('Warden', 'Warden'),
        ('Specialist', 'Specialist')
    ]


    RANGE_TYPE = [
        ('Melee', 'Melee'),
        ('Ranged', 'Ranged'),
        ('Hybrid', 'Hybrid')
    ]

    name = models.CharField(max_length=50, unique=True, verbose_name='Champion Name', help_text='Enter Champion\'s Name')
    champ_Class = models.CharField(max_length=20, choices=CLASSES, verbose_name='Choose Champion\'s Class')
    legacy = models.ManyToManyField(Legacy, help_text='Choose Champion\'s Legacys')
    lanes = models.ManyToManyField(Lanes, help_text='Choose Playable Lanes')
    range_type = models.CharField(max_length=20, choices=RANGE_TYPE, verbose_name='Choose Range Type')
    image = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Náhledový obrázek")
    lore = models.CharField(max_length=800, verbose_name='Champion Lore', blank=True, null=True, help_text='Enter Champion\'s Lore')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

