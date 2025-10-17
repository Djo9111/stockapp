# Guide Django - Système de Gestion de Stock

## 📋 Notes importantes sur la structure du projet

### 1. Navigation dans le projet Django

**Normalement on doit d'abord entrer dans le dossier du projet Django avant de créer une app.**

#### Pourquoi c'est important ?

- Le fichier `manage.py` est dans le dossier du projet → c'est lui qui permet de créer l'app
- Si on ne fait pas `cd stockapp`, on est en dehors du projet et `manage.py` n'est pas accessible

#### Exemple de structure

Quand on fait :
```bash
django-admin startproject erp .
```

On a créé le projet dans le dossier courant `stockapp`, **sans créer un sous-dossier `erp/`**.

**Résultat :** le fichier `manage.py` est dans `D:\Django\stockapp`, pas dans `D:\Django\stockapp\erp`.

---

### 2. Activation de l'app

**Une fois le projet et l'app créés, on doit activer l'app.**

Il faut juste ajouter `stock` dans la liste `INSTALLED_APPS` du fichier `settings.py` :

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stock',  # ← Ajouter votre app ici
]
```

---

### 3. Migrations de base

Après avoir créé vos modèles, exécutez ces commandes dans l'ordre :

```bash
# Créer les fichiers de migration
python manage.py makemigrations

# Appliquer les migrations à la base de données
python manage.py migrate
```

---

## 🔍 Explication du code des modèles

### Résumé du système

Ce code Django gère un **système de gestion de stock** avec suivi des entrées/sorties et calcul du coût des marchandises vendues selon différentes méthodes (FIFO, LIFO, moyenne pondérée).

#### Structure des modèles :

- **Produit** : articles en stock
- **Stock** : lots d'entrée (arrivages) avec leur prix d'achat
- **Mouvement** : enregistrements des entrées/sorties
- **AllocationSortie** : lie les sorties aux lots consommés (traçabilité)

---

## 🎯 Concepts clés Python/Django pour débutants

### 1. **Models et ORM**

```python
class Produit(models.Model):
```

- Les modèles Django = tables de base de données
- Hérite de `models.Model` pour obtenir les fonctionnalités de l'ORM (Object-Relational Mapping)
- Chaque attribut = colonne dans la table

---

### 2. **Types de champs**

| Type de champ | Usage | Exemple |
|---------------|-------|---------|
| `CharField` | Texte court (avec `max_length`) | Nom, description |
| `IntegerField` | Nombres entiers | Quantité, stock |
| `DecimalField` | Nombres décimaux précis | Prix, coûts (important pour l'argent !) |
| `DateField` | Dates | Date d'entrée, date de mouvement |

---

### 3. **Choices (énumérations)**

```python
class MethodeValorisation(models.TextChoices):
    FIFO = "FIFO", "FIFO"
    LIFO = "LIFO", "LIFO"
    MOYENNE = "MOY", "Moyenne pondérée"
```

- `TextChoices` : limite les valeurs possibles (comme une liste déroulante)
- Format : `CODE = "valeur_db", "Label affiché"`
- Évite les erreurs de saisie et standardise les données

---

### 4. **ForeignKey (relations)**

```python
produit = models.ForeignKey(Produit, on_delete=models.PROTECT, related_name="lots")
```

- Crée une relation "plusieurs-à-un" (many-to-one)
- `on_delete=models.PROTECT` : empêche la suppression si des objets liés existent
- `on_delete=models.CASCADE` : supprime en cascade les objets liés
- `related_name="lots"` : accès inverse depuis le modèle parent (`produit.lots.all()`)

**Exemple d'utilisation :**
```python
# Accéder à tous les lots d'un produit
produit = Produit.objects.get(id=1)
lots = produit.lots.all()

# Accéder au produit depuis un lot
lot = Stock.objects.get(id=1)
nom_produit = lot.produit.nom
```

---

### 5. **Meta et optimisation**

```python
class Meta:
    indexes = [
        models.Index(fields=["produit", "date_entree"]),
    ]
```

- `indexes` : accélère les recherches sur certains champs
- Crucial pour les performances sur grandes tables
- Crée des index en base de données pour optimiser les requêtes

---

### 6. **Méthode `__str__`**

```python
def __str__(self):
    return self.nom
```

- Définit comment l'objet s'affiche (dans l'admin Django, les logs, etc.)
- Rend le code plus lisible et facilite le débogage
- Remplace l'affichage par défaut `<Produit object (1)>` par quelque chose de significatif

---

### 7. **Paramètres des champs**

| Paramètre | Signification | Usage |
|-----------|---------------|-------|
| `null=True` | Autorise `NULL` en base de données | Pour les champs optionnels (DB level) |
| `blank=True` | Autorise les champs vides dans les formulaires | Pour la validation Django (Form level) |
| `default` | Valeur par défaut | Valeur automatique si non spécifiée |
| `max_digits` | Nombre total de chiffres | Pour `DecimalField` |
| `decimal_places` | Nombre de décimales | Pour `DecimalField` |

**Important :** Pour les champs optionnels, utilisez souvent `null=True, blank=True` ensemble.

---

## 💡 Points d'attention

Ce système suit les **normes comptables** (FIFO/LIFO/Moyenne pondérée) pour valoriser les stocks :

- **FIFO** (First In, First Out) : Premier entré, premier sorti
- **LIFO** (Last In, First Out) : Dernier entré, premier sorti
- **Moyenne pondérée** : Calcul basé sur le coût moyen

C'est un excellent exemple de **comment lier le code et les besoins métier** dans une application réelle !

---

## 📚 Ressources complémentaires

- [Documentation officielle Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django ORM Cookbook](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/)
- [Django Best Practices](https://learndjango.com/tutorials/django-best-practices-projects-vs-apps)

---

**Date de création :** 17 octobre 2025  
**Auteur :** Documentation du projet Stock Management