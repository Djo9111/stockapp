from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'stock']
        labels = {
            'nom': 'Nom du produit',
            'stock': 'Quantité en stock'
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Mettez le nom ou libellé'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'})
        }