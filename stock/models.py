from django.db import models


# class MethodeValorisation(models.TextChoices):
#     FIFO = "FIFO", "FIFO"
#     LIFO = "LIFO", "LIFO"
#     MOYENNE = "MOY", "Moyenne pondérée"

from django.db import models
from django.core.exceptions import ValidationError


class Stock(models.Model):
    UNIT_CHOICES = [
        ("KG", "Kilogram"),
        ("G", "Gram"),
        ("L", "Liter"),
        ("U", "Unit"),
    ]

    name = models.CharField(max_length=100, unique=True)
    quantite = models.FloatField(default=0)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    min_required = models.FloatField(default=0)
    prix_unitaire = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )  # Prix unitaire
    last_restocked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantite} {self.unit})"

    def ajouter(self, quantite):
        """Ajouter une quantité au stock."""
        if quantite < 0:
            raise ValidationError("La quantité à ajouter doit être positive.")
        self.quantite += quantite
        self.save()

    def retirer(self, quantite):
        """Retirer une quantité du stock."""
        if quantite < 0:
            raise ValidationError("La quantité à retirer doit être positive.")
        if self.quantite - quantite < 0:
            raise ValidationError("Stock insuffisant.")
        self.quantite -= quantite
        self.save()

    def consulter_stock(self):
        """Vérifier si le stock est suffisant par rapport au minimum requis."""
        return self.quantite >= self.min_required

    def valorisation_stock(self):
        """Calculer la valorisation du stock (quantité * prix unitaire)."""
        return self.quantite * self.prix_unitaire


class Produit(models.Model):
    nom = models.CharField(max_length=254)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom

    # Property (attribut calculé)
    # sert à transformer une méthode en attribut accessible sans parenthèses
    @property
    def stockPdt(self):
        return self.stock


class MvtStock(models.Model):
    """Model definition for MvtStock."""

    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveSmallIntegerField()
    sens = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        """Meta definition for MvtStock."""

        verbose_name = "MvtStock"
        verbose_name_plural = "MvtStocks"

    def __str__(self):
        """Unicode representation of MvtStock."""
        pass

    def entrees(self):
        pass

    def sorties(self):
        pass

    def stockactuel(self):
        pass

    def stock_a_date(self, date_stock):
        pass
