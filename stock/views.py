from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm

def liste_produits(request):
    """Affiche la liste de tous les produits"""
    produits = Produit.objects.all()
    return render(request, 'produits/liste.html', {'produits': produits})

def ajouter_produit(request):
    """Ajoute un nouveau produit"""
    if request.method == 'POST':
        # crée un formulaire avec les données envoyées
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'produits/formulaire.html', {'form': form})

def modifier_produit(request, id):
    """Modifie un produit existant"""
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'produits/formulaire.html', {'form': form})

def supprimer_produit(request, id):
    """Supprime un produit"""
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'produits/confirmer_suppression.html', {'produit': produit})
