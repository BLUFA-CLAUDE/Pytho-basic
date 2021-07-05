#Ecrire un programme qui demande à l'utilisateur de saisir un nombre
#entier et lui afficher son factoriel

factoriel =1
nbre = int(input("Tapez un nombre entier: "))
for i in range(1, nbre+1):
    factoriel = factoriel*i
print("Le factoriel de",nbre ,"est:", factoriel)