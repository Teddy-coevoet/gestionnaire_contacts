# Fiche Mémo 1 : Les Bases du Langage Python

## Variables et Types de Données

```python
# Déclaration de variables
x = 5               # entier
y = 3.14            # flottant
name = "Alice"      # chaîne de caractères
is_student = True   # booléen
```

## Types de données courants :

- int : entier
- float : nombre à virgule flottante
- str : chaîne de caractères
- bool : booléen (True or False)

## Opérateurs de Base

```python
# Opérateurs arithmétiques
a = 10
b = 3
addition = a + b        # 13
soustraction = a - b    # 7
multiplication = a * b  # 30
division = a / b        # 3.3333...
modulo = a % b          # 1

# Opérateurs de comparaison
egal = (a == b)         # False
different = (a != b)    # True
plus_grand = (a > b)    # True
plus_petit = (a < b)    # False

# Opérateurs logiques
and_op = True and False  # False
or_op = True or False    # True
not_op = not True        # False
```

# Fiche Mémo 2 : Structures de Contrôle

## Conditions

```python
# Condition if-elif-else
x = 10
if x > 0:
    print("x est positif")
elif x == 0:
    print("x est zéro")
else:
    print("x est négatif")
```

## Boucles

```python
# Boucle for
for i in range(5):  # de 0 à 4
    print(i)

# Boucle while
j = 0
while j < 5:
    print(j)
    j += 1
```

# Fiche Mémo 3 : Listes et Dictionnaires

## Listes

```python
# Déclaration et accès aux éléments
fruits = ["pomme", "banane", "cerise"]
print(fruits[0])  # pomme

# Ajouter et supprimer des éléments
fruits.append("orange")
fruits.remove("banane")
```

## Dictionnaires

```python
# Déclaration et accès aux éléments
etudiant = {"nom": "Alice", "age": 25, "cours": "Python"}
print(etudiant["nom"])  # Alice

# Ajouter et supprimer des éléments
etudiant["ville"] = "Paris"
del etudiant["age"]
```

# Fiche Mémo 4 : Fonctions

## Définition et Appel de Fonction

```python
# Définition d'une fonction
def saluer(nom):
    return f"Bonjour, {nom}!"

# Appel de la fonction
message = saluer("Alice")
print(message)  # Bonjour, Alice!
```

## Fonctions Lambda

```python
# Fonction lambda pour additionner deux nombres
addition = lambda x, y: x + y
print(addition(2, 3))  # 5
```

# Fiche Mémo 5 : Fichiers et Gestion des Erreurs

## Manipulation de Fichiers

```python
# Lecture d'un fichier
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)

# Écriture dans un fichier
with open("fichier.txt", "w") as fichier:
    fichier.write("Bonjour, monde!")
```

## Gestion des Erreurs

```python
# Try-Except pour gérer les exceptions
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : Division par zéro!")
```
