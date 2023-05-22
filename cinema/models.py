from django.db import models

class Actor(models.Model):
    class Meta:
        verbose_name = 'Actor'
        verbose_name_plural = 'Actors'

    name = models.CharField(max_length=24)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name


class Movie(models.Model):

    title = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    release = models.DateField()
    actors = models.ManyToManyField(Actor)

    def __str__(self) -> str:
        return self.title
# Create your models here.
