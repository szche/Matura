with open("DANE/liczby.txt", "r") as file:
    wszystko = [int(line.strip()) for line in file]


def znajdz_dzielniki(liczba):
    dzielniki = [1]
    for i in range(2, (liczba//2)+1):
        if liczba%i == 0:
            dzielniki.append(i)
    dzielniki.append(liczba)
    return dzielniki

wszystkie_dzielniki = []
mniejsze1000 = []
dzielniki_18 = []
for liczba in wszystko:
    if liczba < 1000:
        mniejsze1000.append(liczba)
    dzielniki = znajdz_dzielniki(liczba)
    wszystkie_dzielniki.append(dzielniki)
    if len(dzielniki) == 18:
        dzielniki_18.append(dzielniki)

najwieksza_pierwsza = 0
for x,liczba in enumerate(wszystkie_dzielniki):
    pierwsza = True
    for dzielnik in liczba[1::]:
        for y, liczba2 in enumerate(wszystkie_dzielniki):
            if dzielnik in liczba2 and x != y:
                pierwsza = False
                break
    if pierwsza:
        if liczba[-1] > najwieksza_pierwsza:
            najwieksza_pierwsza = liczba[-1]
        


print("W pliku jest {} liczb mniejszych od 1000, ostatnie dwie to {} i {}".format(len(mniejsze1000), mniejsze1000[-1], mniejsze1000[-2]))
print("Lista liczb majacych 18 dzielnikow:")
for item in dzielniki_18:
    print("Liczba {} ma dzielniki:".format(item[-1]), item)

print("Najwieksza liczba wzlgednie pierwsza to {}".format(najwieksza_pierwsza))
