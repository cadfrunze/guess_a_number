from art import logo
import random
print(logo)

def numarul_ales():
    return random.randint(1, 101)
NUMARUL_ALES = numarul_ales()
numere_alese = 0
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
    while sanse >= 1:
        print(f"Numar incercari: {sanse}")
        alegere_numar = int(input("Alege un numar: "))
        print(f"Ai ales: {alegere_numar}")
        numere_alese = alegere_numar
        if alegere_numar == NUMARUL_ALES:
            return True
        elif alegere_numar < NUMARUL_ALES:
            print("Prea mic...")
        elif alegere_numar > NUMARUL_ALES:
            print("Prea mare....")
        numere_alese = 0
        sanse = sanse - 1
    if sanse < 1:
        return False
final = jocul()
if final == True:
    print(f"Bravo....numarul ales de tine: {numere_alese} s-a potrivit cu numarul ales de calculator ({NUMARUL_ALES})")
else:
    print(f"Imi pare rau...numarul ales de tine: {numere_alese}, nu ai ghicit cu numarul ales de calculator care este {NUMARUL_ALES}")
        



