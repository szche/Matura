liczba_liter = 0
alfabet = {}
samogloski = "AEIOUY"
najdluzsze_podslowo = ""
podslowa = []

with open("DANE/tekst.txt", "r") as file:
    for line in file:
        slowa = line.split()


def uzupelnij_czestosc(slowo):
    for znak in slowo:
        if znak not in alfabet:
            alfabet[znak] = 1
        else:
            alfabet[znak] += 1

def znajdz_podslowo(slowo):
    global najdluzsze_podslowo
    global podslowa
    podslowo = ""
    for znak in slowo:
        if znak not in samogloski:
            podslowo += znak
            if len(podslowo) >= len(najdluzsze_podslowo):
                if len(podslowo) > len(najdluzsze_podslowo):
                    podslowa = []
                najdluzsze_podslowo = podslowo
                if slowo not in podslowa:
                    podslowa.append(slowo)
        else:
            dlugosc = 0
            podslowo = ""

podpunkt_1 = []
for word in slowa:
    znak = word[0]
    for char in word[1::]:
        if znak == char:
            podpunkt_1.append(word)
            break
        znak = char
    uzupelnij_czestosc(word)
    liczba_liter += len(word)
    znajdz_podslowo(word)



print("-" * 40)
print("73.1) Takich slow jest {}".format(len(podpunkt_1)))
print("73.2) Slownik czestosci: ")
for litera in sorted(alfabet):
    print("{}: {} ({}%)".format(litera, alfabet[litera], round((alfabet[litera]/liczba_liter) * 100, 2)))

print("73.3) Najdluzsze podslowo ma {} znakow, pierwsze slowo to {}, a lacznie jest ich {}".format(len(najdluzsze_podslowo), podslowa[0], len(podslowa)))
