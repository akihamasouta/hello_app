from django.db import models

# Create your models here.
class Player_Name(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    job = models.CharField(max_length=15)
    
    def __str__(self):
        return self.job


class Postion(models.Model):
    wolf = models.PositiveIntegerField()
    citizen = models.PositiveIntegerField()
    hunter = models.PositiveIntegerField()
    diviner = models.PositiveIntegerField()
    traitor = models.PositiveIntegerField()
    psychic = models.PositiveIntegerField()
    
    def __int__(self):
        return  None