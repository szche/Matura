with open("DANE/tekst.txt", "r") as file:
    for line in file:
        slowa = line.strip().split()

with open("DANE/probka.txt", "r") as file:
    probka = [line.strip().split() for line in file]


alfabet = "abcdefghijklmnopqrstuvwxyz"

def zaszyfruj(slowo, A, B):
    global alfabet
    wiadomosc = ""
    for znak in slowo:
        litera = ((alfabet.find(znak)*A) + B)%26
        wiadomosc += alfabet[litera]
    return wiadomosc

def odkoduj(tekst1, tekst2):
    global alfabet
    #Zgadywanie A
    for A in range(26):
        #Zgadywanie B
        for B in range(26):
            if zaszyfruj(tekst1, A, B) == tekst2:
                return [A, B]
            

podpunkt_1 = []
podpunkt_2 = []
podpunkt_3 = []

for slowo in slowa:
    if slowo[0] == slowo[-1] and slowo[0] == "d":
        podpunkt_1.append(slowo)
    if len(slowo) >= 10:
        podpunkt_2.append(zaszyfruj(slowo, 5, 2))

for komplet in probka:
    szyfrujacy = odkoduj(komplet[0], komplet[1])
    deszyfrujacy = odkoduj(komplet[1], komplet[0])
    podpunkt_3.append([komplet, szyfrujacy, deszyfrujacy])


print("-" * 40)
print("75.1) Slowa zaczynajace i konczace sie na litere d:")
for slowo in podpunkt_1:
    print(slowo)
print("75.2) Slowa zaszyfrowane o dlugosci conamjniej 10:")
for slowo in podpunkt_2:
    print(slowo)
print("75.3) Slowa wraz z ich kluczami szyfrujacymi i deszyfrujacymi:")
for i in podpunkt_3:
    print("Slowa \"{}\", klucz szyfrujacy {}, klucz deszyfrujacy {}".format(" ".join(i[0]), i[1], i[2]))
