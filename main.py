from math import sqrt

#### Fonction secondaire


def isprime(p):
    if p in [0,1,2]:
        return False
    for i in range(2,p,1):
        if p % i == 0:
            return False
    return True
            
    
    


    # votre code ici

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
