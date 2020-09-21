#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nb = float(input("Veuillez entrez un nombre : "))
    if nb < 0:
        nb = -nb
    return nb


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    listeNoms = []
    for prefixe in prefixes:
        listeNoms.append(prefixe + suffixes)
    return listeNoms


def prime_integer_summation() -> int:
    return 0


def factorial(number: int) -> int:
    factorielle = 1
    i = number
    while i > 0:
        factorielle *= i
        i -= 1
    return factorielle


def use_continue() -> None:
    pass


def main() -> None:
    #print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    #print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    #print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    #print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
