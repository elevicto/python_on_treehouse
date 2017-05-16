# Creation d'une liste
favorite_things = ["sailboat", "les rhododendrons", "les chevaux"]

# Methode 1 pour l'ajout d'un élément à la liste: l'utilisation de "+"
# Avec "+", on ne peut additionner que deux types de données identiques (liste + liste)
favorite_things += ["aviation"] #equivalent à favorite_things = favorite_things + ["aviation"]

#Methode 2 pour l'ajout d'un élément en fin de liste (liste, string, chiffre ou ...?): .append
favorite_things.append(["bright paper packages tied with string"])
#Attention que si on utilises des [], on ajoute une liste à la liste

#Methode 3 pour l'ajout de plusieurs éléments: .extend
favorite_things.extend(["texte 1", "texte 2"])
#ou
favorite_things.extend("abc efg")
#avec .extend sans [], chaque lettre ou espace sera introduit séparément à la liste et donnera par exemple 'a', 'b', 'c', ' ','e', 'f', 'g').

#suppression d'un élément à un endroit précis de la liste par exemple l'avant dernier élément de la liste:
del favorite_things[-2]

#insertion d'un élément à un endroit précis de la liste: .insert. L'inverse de "del"
favorite_things.insert(0, "les violons ivres")

print(favorite_things)

# de manière générale on n'utilise que très rarement "=" car on ne fait que modifier la liste d'origine au lieu de recréer systématiquement des nouvelles listes. C'est une chose pour laquelle il faut rester vigilent.

my_list = [1, 2, 3, 1]
#Remove ne supprime que la première instance d'une valeur d'une liste...
my_list.remove(1)
#Resultat = 2, 3, 1
#Si je relance encore my_list.remove(1), il va supprimer le dernier '1'. Par contre si on continue une 3ème fois, il va retourner une erreur. 
