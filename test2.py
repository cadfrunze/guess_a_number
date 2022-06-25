import time
import os
regulament = "Regulamentul:\n1. Veti fi intrebat de nivelul de dificulate, si va trebui sa alegeti: \"easy\"(10 incercari) sau \"hard\"(5 incercari)\n2. Veti alege un numar de la 1 la 100.\n3. Daca raspunsul nu se afla intre 1 si 100 sau va avea un alt caracter in afara de o cifra, veti fi intrebat din nou fara a se va scadea din incercari.\n4. Cu cat sunteti mai aproape de numarul ales de calculator vi se afisa cate o solutie, respectiv \"Cald!\" sau \"Foarte cald!\"\n4. Cu cat sunteti mai departe vi se va afisa cate o solutie, respectiv: \"Foarte mic!\" sau \"Foarte mare!\""
regulament1 = "Regulamentul:\n"
scriere = ""
for litare in regulament:
    scriere = scriere + litare
    os.system('cls')
    print(scriere)
    time.sleep(0.05)
    if litare == "\n":
        time.sleep(2)