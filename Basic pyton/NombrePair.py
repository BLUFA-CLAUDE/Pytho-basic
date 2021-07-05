#Ecrire un programme que demande à l'utilsateur de saisir un nombre entier
#et de lui affiché si le nombre est pair ou impair

n = int(input("Entrer le nombre n :"))
r = n%2
if(r==0):
    print(n ,"est un nombre paire")
else:
    print(n ,"n'est un nombre impair")