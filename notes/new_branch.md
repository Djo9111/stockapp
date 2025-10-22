# 🌿 Créer et travailler sur une nouvelle branche Git (approche incrémentielle)

Utiliser une **nouvelle branche Git** pour coder de manière incrémentielle (ex : une classe à la fois) est une excellente pratique pour garder ton projet propre et bien organisé.

Voici la **procédure complète étape par étape** 👇

---

## 🧩 1. Se positionner dans ton projet

Ouvre ton terminal dans le dossier de ton projet — c’est-à-dire **l’endroit où se trouve le dossier `.git`**.

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

Par exemple, pour créer une branche `feature-produit` :

```bash
git checkout -b feature-produit
```

🔹 Cela **crée** et te **place** directement dans la nouvelle branche.

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

Tu peux maintenant créer ou modifier du code, par exemple dans un fichier `models/produit.py`.

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

## ⚠️ ⚠️ Si ton `git add .` ne marche pas

Il peut arriver que Git affiche un message comme :

```
no changes added to commit (use "git add" and/or "git commit -a")
```

### 📌 Pourquoi ?

Tu es probablement **dans un sous-dossier** (par exemple `stockapp/stock`) alors que ton dépôt Git (`.git`) est **au niveau supérieur**.
👉 Dans ce cas, `git add .` n’ajoute que les fichiers à l’intérieur du dossier courant, **pas ceux situés plus haut**.

### ✅ Solution 1 — revenir à la racine du projet

Remonte d’un dossier avant d’ajouter :

```bash
cd ..
git add -A
git commit -m "Ajout d'une petite documentation et nettoyage des notes"
```

### ✅ Solution 2 — ajouter explicitement tous les fichiers

Depuis n’importe où dans le dépôt :

```bash
git add -A
git commit -m "Ajout d'une petite documentation et nettoyage des notes"
```

> 🧠 `git add -A` ajoute **tout** : fichiers modifiés, nouveaux et supprimés — même en dehors du dossier courant.

---

## ☁️ 7. Envoyer la branche sur GitHub

```bash
git push -u origin feature-produit
```

Tu verras ensuite ta branche sur GitHub 🎉
GitHub affichera :

> *“feature-produit had recent pushes — Compare & pull request”*

---

## 🔄 8. Revenir sur `main` plus tard

Quand tu voudras revenir à la branche principale :

```bash
git checkout main
```

Et si tu veux fusionner ton travail :

```bash
git merge feature-produit
```

---

## 🚀 Exemple de workflow incrémentiel

| Jour     | Branche            | Tâche                      |
| -------- | ------------------ | -------------------------- |
| Lundi    | `feature-produit`  | Créer la classe `Produit`  |
| Mardi    | `feature-client`   | Ajouter la classe `Client` |
| Mercredi | `feature-commande` | Créer la classe `Commande` |

Chaque branche = une **fonctionnalité isolée** → moins de conflits, commits plus clairs et meilleure collaboration.

---
