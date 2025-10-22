Utiliser une **nouvelle branche Git** pour par exemple coder de manière incrémentielle (ex : une classe à la fois) est une excellente pratique pour garder ton projet propre et bien versionné.

Voici la **procédure complète étape par étape** 👇

---

## 🧩 1. Se positionner dans ton projet

Ouvre ton terminal dans le dossier de ton projet (celui où se trouve ton `.git`).

```bash
cd /chemin/vers/ton/projet

```

Active ton environnement virtuel si besoin :

```bash
source venv/bin/activate        # sous Linux/Mac
# ou
venv\Scripts\activate           # sous Windows

```

---

## 🌱 2. Vérifier ta branche actuelle

Tu peux voir sur quelle branche tu es (souvent `main` ou `master`) :

```bash
git branch

```

Sortie possible :

```
* main

```

---

## 🌿 3. Créer une nouvelle branche

Supposons que tu veux une branche appelée `feature-produit` :

```bash
git checkout -b feature-produit

```

🔹 Cela crée et te place directement dans la branche `feature-produit`.

---

## 💾 4. Vérifier que tu es bien dessus

```bash
git branch

```

Résultat attendu :

```
  main
* feature-produit

```

Le `*` indique la branche active.

---

## 🧱 5. Coder sur ta nouvelle branche

Tu peux maintenant modifier ton code, par exemple ajouter ta classe `Produit` dans un fichier `models/produit.py`.

Exemple :

```python
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def afficher(self):
        return f"{self.nom} coûte {self.prix} FCFA"

```

---

## 💬 6. Ajouter et valider les modifications

Quand tu veux sauvegarder ton travail localement :

```bash
git add .
git commit -m "Ajout de la classe Produit"

```

---

## ☁️ 7. Envoyer la branche sur GitHub

Pour rendre ta branche visible sur GitHub :

```bash
git push -u origin feature-produit

```

Après ça, tu verras la branche sur ton dépôt GitHub 🎉

> (GitHub te proposera même de créer une Pull Request si tu veux fusionner plus tard vers main.)
> 

---

## 🔄 8. Revenir sur `main` plus tard

Quand tu voudras revenir sur la branche principale :

```bash
git checkout main

```

Et si tu veux fusionner ton travail :

```bash
git merge feature-produit

```

---

### 🚀 Exemple de workflow incrémentiel

| Jour | Branche | Tâche |
| --- | --- | --- |
| Lundi | `feature-produit` | Créer la classe `Produit` |
| Mardi | `feature-client` | Ajouter la classe `Client` |
| Mercredi | `feature-commande` | Créer la classe `Commande` |

Chaque branche = une fonctionnalité isolée → moins de conflits et meilleur suivi du code.