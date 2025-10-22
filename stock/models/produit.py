from django.db import models


class MethodeValorisation(models.TextChoices):
    FIFO = "FIFO", "FIFO"
    LIFO = "LIFO", "LIFO"
    MOYENNE = "MOY", "Moyenne pondérée"


class Produit(models.Model):
    nom = models.CharField(max_length=254)
    methode_valorisation = models.CharField(
        max_length=4,
        choices=MethodeValorisation.choices,
        default=MethodeValorisation.FIFO
    )

    def __str__(self):
        return self.nom
