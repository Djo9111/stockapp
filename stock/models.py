from django.db import models


class MethodeValorisation(models.TextChoices):
    FIFO = "FIFO", "FIFO"
    LIFO = "LIFO", "LIFO"
    MOYENNE = "MOY", "Moyenne pondérée"


class TypeMouvement(models.TextChoices):
    ENTREE = "ENTREE", "Entrée"
    SORTIE = "SORTIE", "Sortie"
    AJUSTEMENT = "AJUSTEMENT", "Ajustement"  # (optionnel à l'usage)


class Produit(models.Model):
    nom = models.CharField(max_length=254)
    methode_valorisation = models.CharField(
        max_length=4, choices=MethodeValorisation.choices, default=MethodeValorisation.FIFO
    )
    """"
    # Optionnels (si tu veux les stocker physiquement ; sinon retire-les)
    cout_moyen_courant = models.DecimalField(max_digits=14, decimal_places=6, null=True, blank=True)
    stock_courant = models.IntegerField(null=True, blank=True) """

    def __str__(self):
        return self.nom


class Stock(models.Model):
    """Lot physique reçu (arrivage)."""
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT, related_name="lots")
    date_entree = models.DateField()
    quantite_initiale = models.IntegerField()
    quantite_restante = models.IntegerField()
    prix_achat_unitaire = models.DecimalField(max_digits=14, decimal_places=6)

    class Meta:
        indexes = [
            models.Index(fields=["produit", "date_entree"]),
        ]


class Mouvement(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT, related_name="mouvements")
    date_mouvement = models.DateField()
    type = models.CharField(max_length=12, choices=TypeMouvement.choices)
    quantite = models.IntegerField()
    prix_vente_unitaire = models.DecimalField(max_digits=14, decimal_places=6, null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["produit", "date_mouvement"]),
            models.Index(fields=["type"]),
        ]


class AllocationSortie(models.Model):
    """Détail du lien entre une sortie et les lots utilisés."""
    mouvement = models.ForeignKey(
        Mouvement, on_delete=models.CASCADE, related_name="allocations"
    )
    lot = models.ForeignKey(
        Stock, on_delete=models.PROTECT, related_name="allocations"
    )
    quantite_allouee = models.IntegerField()
    prix_cout_unitaire = models.DecimalField(max_digits=14, decimal_places=6)

    class Meta:
        indexes = [
            models.Index(fields=["mouvement"]),
            models.Index(fields=["lot"]),
        ]
