import math
with open("dane/dane_systemy1.txt", "r") as plik1:
    stacja1 = [line.strip().split() for line in plik1]

with open("dane/dane_systemy2.txt", "r") as plik2:
    stacja2 = [line.strip().split() for line in plik2]

with open("dane/dane_systemy3.txt", "r") as plik3:
    stacja3 = [line.strip().split() for line in plik3]

def wartosc_bezwzgledna(liczba):
    if liczba < 0:
        return -liczba
    return liczba


def znajdz_najmniejsza(system, tablica):
    najmniej = int(tablica[0][1], system)
    for item in tablica:
        if int(item[1], system) < najmniej:
            najmniej = int(item[1],system)
    return najmniej

def blad_pomiaru(system, tablica):
    pierwszy = int(tablica[0][0], system)
    pomylki = [0 for item in tablica]
    #print(pierwszy)
    for counter, item in enumerate(tablica[1::]):
        #print(int(item[0], system))
        if pierwszy +24 != int(item[0], system):
            pomylki[counter+1] = 1
        pierwszy += 24
    return pomylki

def rekordy_temperatury(system, tablica):
    pierwsza = int(tablica[0][1], system)
    rekordy = [pierwsza]
    for item in tablica[1::]:
        if int(item[1], system) > pierwsza:
            pierwsza = int(item[1], system)
            rekordy.append(pierwsza)
        else:
            rekordy.append('-')
    return rekordy

def skoki_temperatury(system, tablica):
    najwiekszy_skok = 0
    for x, item in enumerate(tablica):
        temp1 = int(item[1], system)
        #print(temp1)
        for y, check in enumerate(tablica[x+1::]):
            indeksY = x+1+y+1
            temp2 = int(check[1], system)
            #print(temp2)
            roznicaTemp = (temp1 - temp2)*(temp1 - temp2)
            roznicaIndeks = wartosc_bezwzgledna((x+1)-indeksY)
            skok = roznicaTemp / roznicaIndeks
            if math.ceil(skok) > najwiekszy_skok:
                najwiekszy_skok = math.ceil(skok)

    return najwiekszy_skok
    
print("-" * 40)
najmniej1 = znajdz_najmniejsza(2, stacja1)
najmniej2 = znajdz_najmniejsza(4, stacja2)
najmniej3 = znajdz_najmniejsza(8, stacja3)

print("Najnizsze temperatury\nStacja1: {}\nStacja2: {}\nStacja3: {}\n".format("{0:b}".format(najmniej1), "{0:b}".format(najmniej2), "{0:b}".format(najmniej3))+"-"*30)

pomiary1 = blad_pomiaru(2, stacja1)
pomiary2 = blad_pomiaru(4, stacja2)
pomiary3 = blad_pomiaru(8, stacja3)
lacznie_pomylki = 0
for counter, x in enumerate(pomiary1):
    if x == 1 and pomiary2[counter] == 1 and pomiary3[counter] == 1:
        lacznie_pomylki += 1

print("Liczba dni, w których stan zegarów był niepoprawny: {}".format(lacznie_pomylki))
print("-" * 40)

rekordy1 = rekordy_temperatury(2, stacja1)
rekordy2 = rekordy_temperatury(4, stacja2)
rekordy3 = rekordy_temperatury(8, stacja3)
dni_rekordowych = 0
for counter, x in enumerate(rekordy1):
    if x != '-' or rekordy2[counter] != '-' or rekordy3[counter] != '-':
        dni_rekordowych += 1

print("Liczba dni rekordów: {}".format(dni_rekordowych))
print("-" * 40)

skok1 = skoki_temperatury(2, stacja1)
print("Największy skok temperatury: {}".format(skok1))
print("-" * 40)
