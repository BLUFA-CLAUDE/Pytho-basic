#Ecrire un programme en python qui demande à l'utilisateur de saisir
#une chaine de caractère et de lui renvoyer un message indiquant si 
#la chaine contient la lettre a, tout en indiquant sa position sur la chaine
phrase = input("Entrer la phrase à examiner: ")
taille = len(phrase)
for i in range(0, taille):
    if(phrase[i]=='a'):
        print("La lettre a se trouve à la position: ",i)