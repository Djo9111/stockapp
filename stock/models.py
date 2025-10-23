from django.db import models


# class MethodeValorisation(models.TextChoices):
#     FIFO = "FIFO", "FIFO"
#     LIFO = "LIFO", "LIFO"
#     MOYENNE = "MOY", "Moyenne pondérée"


class Produit(models.Model):
    nom = models.CharField(max_length=254)
    stock = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom

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
