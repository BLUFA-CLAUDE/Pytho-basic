def suiteNumerique(nbre):
    somme = []
    for k in range(1, nbre+1):
        somme.append((k**k)/(nbre**nbre))
    print(somme)
    monotone = True
    if somme[0]>=somme[1]:
        for i in range(1, nbre-1):
            if somme[i]<=somme[i+1]:
                monotone = False
                break
    else:
        for i in range(1, nbre-1):
            if somme[i]>=somme[i+1]:
                monotone = False
                break
    return monotone


nbre =int(input("Saisir la taille du liste: "))
print(suiteNumerique(nbre))