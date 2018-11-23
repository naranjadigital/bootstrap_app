from django.db import models

# Create your models here.

CHOICES = [
    ('A', 'Letra A' ),
    ('B', 'Letra B' ),
    ('C', 'Letra C' ),
]


class Foranea(models.Model):
    nombre = models.CharField(max_length=50)


class Crud(models.Model):
    codigo = models.CharField(max_length=5, null=True, blank=True)
    nombre = models.CharField(max_length=50)
    foranea = models.ForeignKey(Foranea, on_delete=models.CASCADE, null=True, blank=True)
    entero = models.IntegerField(default=0)
    choice = models.CharField(max_length=1, choices=CHOICES)
