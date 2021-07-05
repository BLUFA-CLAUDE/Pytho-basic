

#fonction factoriel
def factoriel(n):
    if n==0 or n==1:
         return 1
    else:
        resultat= 1
        for i in range(n+1):
            resultat*=i
        return resultat

def binomiale(n,p):
    resultat=0
    if 0<=p<=n :
        resultat= factoriel(n)/(factoriel(p)*factoriel(n-p))
    return resultat

def maxbinomiale(n):
    maxi=binomiale(n,0)
    for p in range(1,n+1):
        val = binomiale(n,p)
        if val>maxi:
            maxi=val
    return maxi

def verifemaxbinomiale(n):
    maxi = maxbinomiale(n)
    va = binomiale(n,n//2)
    return maxi==va

