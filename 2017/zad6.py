with open("DANE/dane.txt", "r") as file:
    wszystko = [line.strip().split() for line in file]


def wartosc_bezwzledna(liczba):
    if liczba < 0:
        return -liczba
    else:
        return liczba


najjasniejszy = int(wszystko[0][0])
najciemniejszy = int(wszystko[0][0])

nalezy_usunac_symetria = 0
kontrastujace = 0
for licznik1, line in enumerate(wszystko):

    for licznik2, piksel in enumerate(line):
        if int(piksel) > najjasniejszy:
            najjasniejszy = int(piksel)
        elif int(piksel) < najciemniejszy:
            najciemniejszy = int(piksel)

        # Ten sam wiersz, poprzedni piksel
        if wartosc_bezwzledna(int(piksel) - int(line[licznik2-1])) > 128 and licznik2 != 0:
            kontrastujace += 1
        #Ten sam wiersz, nastepny piksel
        elif licznik2 != 319 and wartosc_bezwzledna(int(piksel) - int(line[licznik2+1])) > 128:
            kontrastujace += 1
        # Wiersz wyżej
        elif licznik1 != 0 and wartosc_bezwzledna(int(piksel) - int(wszystko[licznik1-1][licznik2])) > 128:
            kontrastujace += 1
        # Wiersz niżej
        elif licznik1 != 199 and wartosc_bezwzledna(int(piksel) - int(wszystko[licznik1+1][licznik2])) > 128:
            kontrastujace += 1

    if line != line[::-1]:
        nalezy_usunac_symetria +=1

#Szukanie najdluzszego ciagu
najdluzszy_ciag = 0
for x in range(0, 320):
    poprzedni = wszystko[0][x]
    czestosc = 1
    for i in range(1, 200):
        if int(poprzedni) == int(wszystko[i][x]):
            czestosc += 1
        else:
            if czestosc > najdluzszy_ciag:
                najdluzszy_ciag = czestosc
            czestosc = 1
        poprzedni = wszystko[i][x]

with open("wyniki6.txt", "w") as wyniki:
    wyniki.write("6.1) Najjasniejszy piksel {}\n".format(najjasniejszy))
    wyniki.write("Najciemniejszy piksel {}\n".format(najciemniejszy))
    wyniki.write("6.2) Nalezy usunac {}\n".format(nalezy_usunac_symetria))
    wyniki.write("6.3) Istnieje {} kontrastujacych pikseli\n".format(kontrastujace))
    wyniki.write("6.4) Najdluzszy ciag ma dlugosc {}\n".format(najdluzszy_ciag))
