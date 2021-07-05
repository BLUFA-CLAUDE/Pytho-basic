#Definition d'un dictionnnaire vide

d1={}
d2=dict()

#Definition d'un dictionnnaire avec initialisaton de valeurs

d3={'nom':'Fall', 'prenom':'Moussa', 'classe':'DITI4'}

print(f"L'etudiant {d3['prenom']} {d3.get('nom')} est inscrit en {d3['classe']}")

#Insertion de données
#print(d2)
#d2 contient les notes
d2['python']=12
d2['java']=16
d2['php']=18
#print(d2)

d1['etudiant']=d3
d1['note']=d2
#print(d1)

#Recuperer la liste des clés
#print("les clés de D3: ",d3.keys())

#Recuperer la liste des valeurs
#print("les valeurs de D3: ",d3.values())

#Recuperer des clés et valeurs
#print("les clés de D3: ",d3.items())

#Parcourir un dictionnaire: Technique 1

print("Technique 1")
for i in d3.keys():
    print(f" La valeur {d3.get(i)} est associée à la clé {i}")

print()

print("Technique 2")
for i in d3.values():
    print(i, end="***")

print()

print("Technique 3")
for i,j in d3.items():
    print(f" La valeur {j} est associée à la clé {i}")
