import sys
import time


def diviseurs_propres(n):
    """Les diviseurs propres de n sont ses diviseurs sauf lui-meme"""
    return [1] + [x for x in range(2, n // 2 + 1) if n % x == 0]


def premier(n):
    """n est premier s'il n'est divisible que par 1 et lui-même
       autrement dit, s'il n'a pas de diviseur propres à part 1"""
    return diviseurs_propres(n) == [1]


def chanceux(n):
    """n est chanceux si n + i^2 + i est premier pour i de 0 à n-2
       Il a été prouvé qu'il n'y en a que 6 : 2, 3, 5, 11, 17 et 41"""
    est_chanceux = True
    for i in range(n - 1):
        est_chanceux = est_chanceux and premier(n + i + i * i)
    return est_chanceux


def parfait(x):
    """x est parfait s'il est égal à la somme de ses diviseurs propres"""
    return x == sum(diviseurs_propres(x))


def tous(pred, n):
    """Renvoie la liste des nombres de 2 à n vérifiant pred
    """
    return [x for x in range(2, n + 1) if pred(x)]


def premiers(limite):
    return tous(premier, limite)


def parfaits(limite):
    return tous(parfait, limite)


def tous_chanceux(limite):
    return tous(chanceux, limite)


def amis(limite):
    """x et y sont amis si la somme des diviseurs propres de x = y et si
       la somme des diviseurs propres de y = x
    """
    return [(x, y)
            for x in range(2, limite + 1)
            for y in [sum(diviseurs_propres(x))]
            if y > x and x == sum(diviseurs_propres(y))]


# Crible d'Erathostène original : pas de division ni multiplication...
def erathos(limite):
    crible = [True] * (limite + 1)   # Initialisation du crible
    crible[0:2] = [False, False]     # 0 et 1 ne sont pas premiers
    premiers = []
    for nbre, marque in enumerate(crible):
        if marque:
            premiers.append(nbre)
            # on met à False les "multiples de nbre"
            for multiple in range(nbre + nbre, limite + 1, nbre):
                crible[multiple] = False
    return premiers


def decale(car, offset, base):
    """Décale car de offset positions vers la droite.
       base est le premier caractère de l'alphabet : A ou a"""
    return chr(ord(base) + (ord(car) - ord(base) + offset) % 26)


def encode(mess, shift):
    result = ''
    for c in mess:
        if 'a' <= c <= 'z': 
            result += decale(c, shift, 'a')
        elif 'A' <= c <= 'Z': 
            result += decale(c, shift, 'A')
        else:
            result += c
    return result


def decode(mess, shift):
    return encode(mess, -shift)


def rot13(mess):
    return encode(mess, 13)


# fonctions utilitaires

def _timing(func, param, output=False):
    """Mesure et affiche le temps d'exécution de l'appel func(param).
       Si output vaut True, affiche aussi le résultat de func(param)
    """
    start = time.time()
    res = func(param)
    print("{}({}) exécuté en {:1.4f} secondes".
          format(func.__name__, param, time.time() - start))
    if output:
        print(res)


def _usage():
    print("Usage: {} <nb> avec nb >= 2".format(sys.argv[0]), file=sys.stderr)
    sys.exit(1)


# Programme principal
if __name__ == '__main__':

    limite = 0

    if len(sys.argv) == 2:
        # Traitement du paramètre qui doit être un entier >= 2...
        try:
            limite = int(sys.argv[1])
            if limite < 2:
                raise ValueError
        except ValueError:
            _usage()

    elif len(sys.argv) == 1:
        # Demande la limite à l'utilisateur (entier >= 2)
        while True:
            try:
                limite = int(input("Entrer un entier >= 2 : "))
                if limite < 2:
                    raise ValueError
                else:
                    break
            except ValueError:
                pass

    else:  # Plus d'un paramètre...
        _usage()

    assert limite >= 2

    # timing des fonctions

    _timing(premiers, limite)

    _timing(erathos, limite)

    _timing(parfaits, limite)

    _timing(amis, limite)

    _timing(tous_chanceux, limite)
