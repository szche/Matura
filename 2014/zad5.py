
napisy_pierwsze = []
napisy_rosnace = []
wszystkie = []
wiecej_niz_raz = []

def czy_pierwsza(liczba):
    pierwsza = True
    for i in range(2, liczba//2):
        if liczba % i == 0:
            pierwsza = False
            break
    return pierwsza

def czy_rosnacy(kody):
    nastepny_kod = kody[0]
    for item in kody[1:]:
        if item > nastepny_kod:
            nastepny_kod = item
        else:
            return False

    return True

def napis_pierwszy(napis):
    kody_ascii = []
    suma_ascii = 0
    for char in napis:
        suma_ascii += ord(char)
        kody_ascii.append(ord(char))

    return czy_pierwsza(suma_ascii)
    return czy_rosnacy(kody_ascii)


with open("DANE/NAPIS.TXT", "r") as file:
    for line in file:
        if line.endswith("\n"):
            line = line[:len(line) - 1]

        # A)
        if napis_pierwszy(line):
            napisy_pierwsze.append(line)

        # B)
        if czy_rosnacy(line):
            napisy_rosnace.append(line)

        # C)
        if line not in wszystkie:
            wszystkie.append(line)
        else:
            wiecej_niz_raz.append(line)


print("-" * 40)
print("WYNIKI")
print("a)",len(napisy_pierwsze))
print("b)", napisy_rosnace)
print("c)", wiecej_niz_raz)
