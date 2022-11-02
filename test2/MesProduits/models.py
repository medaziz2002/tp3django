from django.db import models

class Produits(models.Model):
    nom = models.CharField(max_length=50)
    realisateur = models.CharField(max_length=50)
    prix = models.FloatField()
    datedecreation = models.DateField()

