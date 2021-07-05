#Ecris un programme qui demande à l'utilisateur de saisir un nombre
#et de lui afficher la somme 1+2....+n=

somme = 0
nbre = int(input("Tapez le nombre entier naturel: "))
for i in range(0, nbre+1):
    somme = somme+i
print("La somme est: ", somme)