#Ecrire un programme qui demande à l'utilisateur de saisir son age
#et de lui afficher le message <<Vous etes Majeur>> Si l'age tapée est
#superieur ou egal à 18. et le message <<Vous etes Mineur>> si l'age
#tapée est inferieur à 18

age = int(input("Tapez votre age: "))
if age>= 18:
    print("Vous etes Majeur")
else:
    print("Vous etes Mineur")