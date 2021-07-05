#Une fonction qui recherche un element dans une liste

def SearchElemment(i,L):
    for k in range(len(L)):
        if L[k]==i:
            return (k)
    return (False)

#liste = ["jean","kaba",12]
#indice ="m"
#resulta = SearchElemment(indice,liste)
#print(resulta)

def maximum(L):
    m=L[0]
    ind=0
    for k in range(len(L)-1):
        if m<=L[k+1]:
            m=L[k+1]
            ind = k+1
    return (m,ind)
liste = [1,8,0,34,89]
kaba = maximum(liste)
print(kaba)
