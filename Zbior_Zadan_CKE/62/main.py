with open("DANE/liczby1.txt", "r") as plik8:
    liczby8 = [int(line.strip(), 8) for line in plik8]

with open("DANE/liczby2.txt", "r") as plik10:
    liczby10 = [int(line.strip()) for line in plik10]


def znajdz_ciag(tablica):
    ciag = [tablica[0]]
    najdluzszy = [tablica[0]]
    dlugosc = 1
    for item in tablica[1::]:
        if item >= ciag[-1]:
            dlugosc += 1
            ciag.append(item)
        else:
            if len(ciag) > len(najdluzszy):
                najdluzszy = [item for item in ciag]
            dlugosc = 1
            ciag = [item]
    return najdluzszy

def porownanie(tablica1, tablica2):
    jednakowa_wartosc = 0
    wieksze_od_2 = 0
    for counter, item1 in enumerate(tablica1):
        if item1 == tablica2[counter]:
            jednakowa_wartosc += 1
        elif item1 > tablica2[counter]:
            wieksze_od_2 += 1
    return [jednakowa_wartosc, wieksze_od_2]


def wystepowanie8(tablica):
    wystepowanie_10 = 0
    wystepowanie_8 = 0
    for item in tablica:
        wystepowanie_10 += str(item).count("6")
        wystepowanie_8 += "{0:o}".format(item).count("6")
    return [wystepowanie_10, wystepowanie_8]


print("-" * 40)
najwieksza8 = max(liczby8)
najmniejsza8 = min(liczby8)
print("Najwieksza liczba to {}, a najmniejsza to {}".format("{0:o}".format(najwieksza8), "{0:o}".format(najmniejsza8)))
print("-" * 40)

ciag10 = znajdz_ciag(liczby10)
print("Najlduzszy ciag rozpoczyna sie od {} i ma dlugosc {} elementow".format(ciag10[0], len(ciag10)))
print("-" * 40)

wynik_porownania = porownanie(liczby8, liczby10)
print("{} liczb ma taka sama wartosc, {} liczb z liczby1 jest wieksze od liczby2".format(wynik_porownania[0], wynik_porownania[1]))
print("-" * 40)

wynik_wystepowania = wystepowanie8(liczby10)
print("W zapisie dziesietnym wystepuje {} liczb, a w osemkowym {} liczb".format(wynik_wystepowania[0], wynik_wystepowania[1]))
print("-" * 40)
