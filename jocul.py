from numbers import Number
from art import logo
import random
import string
print(logo)
TABEL_CARACTERE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',]
TABEL_NUMERE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "", " "]
def numarul_ales():
    return random.randint(1, 100)
NUMARUL_ALES = numarul_ales()
numere_alese = []
def jocul():
    print("Bine ai venit la jocul \"Ghiceste numarul\"")
    print(f"Psst numarul ales de calculator este: \"{NUMARUL_ALES}\"")
    alegere_nivel = input("Alege nivelul de dificultate. Scrie \"easy\" sau \"hard\": ").lower()
    sanse = 0

    while alegere_nivel != "easy" and alegere_nivel != "hard":
        alegere_nivel = input("Nu am inteles. Alege nivelul de dificultate. Scrie \"easy\" sau \"hard\": ").lower()
    if alegere_nivel == "easy":
        sanse = sanse + 10
    elif alegere_nivel == "hard":
        sanse = sanse + 5
    game0 = True
    print("-" * 20)
    print(f"Numar incercari: {sanse}")
    alegere_numar = input("Alege un numar: ")
    while sanse >= 1:
        if len(alegere_numar) == 0:
            alegere_numar = input("Te rog sa scri o cifra. Alege un numar de la 1 la 100: ")
        elif len(alegere_numar) > 3:
            alegere_numar = input("Ai introdus prea multe caractere!. Alege un numar de la 1 la 100: ")
        for i in alegere_numar:
            if i in TABEL_CARACTERE:
                alegere_numar = input(f"Hey! Vezi ca nu ai scris o cifra. Alege un numar de la 1 la 100: ")
                game0 = False
        for a in alegere_numar:
            if a not in TABEL_CARACTERE:
                game0 = True
        if game0 == True:
            alegere_numar = int(alegere_numar)
            while alegere_numar in numere_alese:
                    alegere_numar = int(input(f"Hey! Vezi ca ai mai scris acest numar ({numere_alese[-1]}). Alege un alt numar: "))
            numere_alese.append(alegere_numar)
            while alegere_numar > 100 or alegere_numar < 1:
                if alegere_numar > 100:
                    alegere_numar = input(f"Hey! Vezi ca ai mai scris un numar mai mare ca si 100. Alege un numar de la 1 la 100: ")
                else:
                    alegere_numar = input(f"Hey! Vezi ca ai mai scris un numar mai mic ca si 1. Alege un numar de la 1 la 100: ")
            print(f"Ai ales: {numere_alese[-1]}")
            if alegere_numar == NUMARUL_ALES:
                return True
            elif alegere_numar < NUMARUL_ALES:
                if (NUMARUL_ALES - int(numere_alese[-1])) <= 10:
                    if (NUMARUL_ALES - int(numere_alese[-1])) <= 5:
                        print("Foarte cald!")
                    else:
                        print("Cald")
                else:
                    print("Prea mic!")
            elif alegere_numar > NUMARUL_ALES:
                if (int(numere_alese[-1] - NUMARUL_ALES)) <= 10:
                    if (int(numere_alese[-1] - NUMARUL_ALES)) <= 5:
                        print("Foarte cald!")
                    else:
                        print("Cald")
                else:
                    print("Prea mare!")
            sanse = sanse - 1
            print("-" * 20)
            print(f"Numar incercari: {sanse}")
            alegere_numar = input("Alege un numar: ")
        if sanse < 1:
            return False
final = jocul()
if final == True:
    print(f"Bravo....numarul ales de tine: {numere_alese[-1]} s-a potrivit cu numarul ales de calculator ({NUMARUL_ALES})")
else:
    print(f"Imi pare rau...numarul ales de tine: {numere_alese[-1]}, nu ai ghicit cu numarul ales de calculator care este {NUMARUL_ALES}")
        