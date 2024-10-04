'''
Programme trouvant tous les nombres premiers de 0 a 100.
'''

from math import sqrt

#### Fonction secondaire


def isprime(n):
    # votre code ici
    '''
    Retourne si le nombre n est premier ou pas.

    Args:
        n: entier naturel.

    Returns:
        True: Booléen, si n est premier.
        False: Booléen, si n n'est pas premier.
    '''
    if n in (0, 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

#### Fonction principale


def main():
    '''
    Fonction principale
    '''

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
