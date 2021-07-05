#Ecrire un programme qui permet de compter le nombre de voyelle
#dans une chaine donnée: Exemple pour la chaine <<anticonstitutionnellement>>
#le programme doit revoyer le message suivant:
#La chaine anticonstitutionnellement contient 10 voyelles
chaine = "anticonstitutionnellement"
taille = len(chaine)
nbVoyelle = 0
for i in range(0, taille):
    if(chaine[i] in ['a','e','i','u','o','y']):
        nbVoyelle = nbVoyelle+1
print("la nombre de voyelle est: ",nbVoyelle)