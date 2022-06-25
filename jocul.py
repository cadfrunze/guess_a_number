from art import logo
import random
print(logo)
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
    game0 = True
    while sanse >= 1:
        alegere_numar = input("Alege un numar: ")
        while game0:
            user_proba = []
            for i in alegere_numar:
                user_proba.append(i)
                if i == " ":
                    user_proba.remove(i)
            alegere_numar = "".join(user_proba)
            print(alegere_numar)
            if alegere_numar.isnumeric():
                alegere_numar = int(alegere_numar)
                if alegere_numar > 100 or alegere_numar < 1:
                    if alegere_numar > 100:
                        alegere_numar = input(f"Hey! Vezi ca ai scris un numar mai mare ca si 100. Alege un numar de la 1 la 100: ")
                        continue
                else:
                    alegere_numar = input(f"Hey! Vezi ca ai mai scris un numar mai mic ca si 1. Alege un numar de la 1 la 100: ")
                    continue
                game0 = False
                game1 = True
            else:
                alegere_numar = input(f"Hey! Vezi ca nu ai scris o cifra. Alege un numar de la 1 la 100: ")
                game1 = False
                continue
            
                
        if game1 == True:
            numere_alese.append(alegere_numar)
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
            game1 = False
            game0 = True
        if sanse < 1:
            return False
final = jocul()
if final == True:
    print(f"Bravo....numarul ales de tine: {numere_alese[-1]} s-a potrivit cu numarul ales de calculator ({NUMARUL_ALES})")
else:
    print(f"Imi pare rau...numarul ales de tine: {numere_alese[-1]}, nu ai ghicit cu numarul ales de calculator care este {NUMARUL_ALES}")
        