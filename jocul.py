from numbers import Number
from pickle import TRUE
from art import logo
import random
import string
print(logo)
TABEL_CARACTERE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',]
TABEL_NUMERE = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', 
'75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101'
]
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
    print("-" * 20)
    print(f"Numar incercari: {sanse}")
    alegere_numar = input("Alege un numar: ")
    while sanse >= 1:
        if len(alegere_numar) == 0:
            alegere_numar = input("Te rog sa scri o cifra. Alege un numar de la 1 la 100: ")
        elif len(alegere_numar) > 3:
            alegere_numar = input("Ai introdus prea multe caractere!. Alege un numar de la 1 la 100: ")
        for i in alegere_numar:
            user_proba = []
            user_proba.append(i)
            proba = 0
            if i in TABEL_CARACTERE:
                alegere_numar = input(f"Hey! Vezi ca nu ai scris o cifra. Alege un numar de la 1 la 100: ")
                game0 = False
            elif i == " ":
                user_proba.remove(i)
                len(alegere_numar) + 1
            if i in TABEL_NUMERE:  
                proba = proba + 1
            if proba == len(alegere_numar):
                alegere_numar = "".join(user_proba)
                while alegere_numar in numere_alese:
                    alegere_numar = input(f"Hey! Vezi ca ai mai scris acest numar ({numere_alese[-1]}). Alege un alt numar: ")
                    game0 = False
                while alegere_numar not in TABEL_NUMERE:
                    game0 = False
                if alegere_numar in TABEL_NUMERE:
                    game0 = True
        print(alegere_numar)  
        if game0 == True:
            numere_alese.append(alegere_numar)
            alegere_numar = int(alegere_numar)
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
        