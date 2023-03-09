from django.db import models
from django.conf import settings

# Create your models here.

class Judge(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)

class Player(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    club_name = models.CharField(max_length=255)

    judge = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    eliminations_score = models.CharField(max_length=255, default="-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1")

    def __str__(self):
        return f'{self.name} {self.surname} ({self.license_number})'

class Session(models.Model):
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    players = models.ManyToManyField(Player)
    judges = models.ManyToManyField(settings.AUTH_USER_MODEL)
    status = models.CharField(max_length=255, default='lobby') #lobby, active, ended
