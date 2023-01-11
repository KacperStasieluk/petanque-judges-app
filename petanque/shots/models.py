from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)
    club_name = models.CharField(max_length=255)

class Judge(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)

class Session(models.Model):
    code = models.CharField(max_length=255)
    players = models.ManyToManyField(Player)
    judges = models.ManyToManyField(Judge)
    status = models.CharField(max_length=255)
