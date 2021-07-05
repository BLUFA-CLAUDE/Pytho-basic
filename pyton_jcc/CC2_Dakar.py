import math
#a = int(input("Saisir la va leur de a: "))
#b = int(input("Saisir la va leur de b: "))
#c = int(input("Saisir la va leur de c: "))

def formuleHerons(a,b,c):
    p = a+b+c
    s = p/2
    nbre = s*(s-a)*(s-b)*(s-c)
    resultat = math.sqrt(nbre)
    print(resultat)

#formuleHerons(a,b,c)

def booleaMemesigne(a,b):
    resultat = a>0 and b>0 or a==0 and b==0 or a==0 and b>0 or a>0 and b==0 or a<0 and b==0 or a==0 and b<0
    if resultat:
        return True
    else:
        return False

    
#print(booleaMemesigne(a,b))

def sommePremierNre(a):
    if a>=0:
        s=0
        for i in range(1, a+1):
            s = s+i
        
        b= a*(a+1)/2
        if s==b:
            return s

#print(sommePremierNre(a))

def echangeListe(nbre):
    while(nbre<=0):
        nbre = int(input("Saisir la taille de la liste: "))
    liste =[]
    for i in range(1, nbre+1):
        valeur = int(input("Saisir le nombre: "))
        liste.append(valeur)
    print(liste)
    premier = liste[0]
    dernier = liste[nbre-1]
    liste[0]=dernier
    liste[nbre-1]=premier
    print(liste)

#nbre = int(input("Saisir la taille de la liste: "))     
#echangeListe(nbre)

def patineListe():
    nbre = int(input("Saisir la taille de la liste: "))
    liste = []
    for i in range(1, nbre+1):
        valeur = int(input("Saisir le nombre: "))
        liste.append(valeur)
    print(liste)
    indice = int(input("Saisir l'indice de la liste: "))
    if liste[indice-1]==liste[indice+1]:
        return True
    else:
        return False


#print(patineListe())

def repeterListe():
    nbre = int(input("Saisir la taille de la liste: "))
    liste = []
    for i in range(1, nbre+1):
        valeur = int(input("Saisir le nombre: "))
        liste.append(valeur)
    print(liste)
    M = []
    for i in range(0, nbre):
        M.append(liste[i])
    for i in range(0, nbre):
        M.append(liste[i])
    print(liste)
    print(M)
  
#repeterListe()

def listeCroissant():
    nbre = int(input("Saisir la taille de la liste: "))
    liste = []
    for i in range(1, nbre+1):
        valeur = int(input("Saisir le nombre: "))
        liste.append(valeur)
    print(liste)
    croissant =[]
    croissant = sorted(liste)
    print(croissant)
    if croissant==liste:
        return True
    else:
        return False

#print(listeCroissant())

def aireDisque(r):
    s = 3.14*r*r
    return (s)

#nbre = int(input("Saisir le rayon du disque: "))
#print(aireDisque(nbre))

def volumeCylindre(r, h):
    S = aireDisque(r)
    V = S*h
    return (V)

#r = int(input("Saisir le rayon du disque: "))
#h = int(input("Saisir la haureur du disque: "))
#print(volumeCylindre(r, h))

def afficheLitre(v):
    print(f"volume: {v} Litre")

#v = int(input("Saisir le volume: "))
afficheLitre(volumeCylindre(4,12)+volumeCylindre(2,8))

