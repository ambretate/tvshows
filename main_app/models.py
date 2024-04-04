from django.db import models
from datetime import date

# Create your models here.
# STARS = (
#     (0, 'No recommendation'),
#     (1, 'Meh'),
#     (2, 'Some redeeming moments but not great'),
#     (3, 'Good'),
#     (4, 'Highly recommend!')

# )

class Cast(models.Model):
    actor = models.CharField(max_length=200)

class TVshow(models.Model):
    name = models.CharField(max_length=None)
    provider = models.CharField(max_length=100)
    review = models.CharField(max_length = None)
    actors = models.ManyToManyField(Cast)

    def __str__(self):
        return self.name

class Viewing(models.Model):
    season = models.PositiveSmallIntegerField()
    epiosde = models.PositiveSmallIntegerField()
    date = models.DateField('Viewing Date')
    
    show = models.ForeignKey(TVshow, on_delete=models.CASCADE)

    class Star(models.IntegerChoices):
        ZERO_STARS = 0
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4

    stars= models.IntegerField(choices=Star.choices)

    def __str__(self):
        return f'{self.show} Season {self.season} Episode {self.epiosde}'
    
    class Meta: 
        ordering = ['-date']
    
    
