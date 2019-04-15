with open("DANE/dane.txt", "r") as file:
    glosowanie = [line.strip().split() for line in file]

lacznie_glosy_komitety = [0, 0, 0, 0, 0, 0]
komitety = ["A", "B", "C", "D", "E", "F"]
lacznie_glosy_okregi = []
lacznie_mandaty = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0
    }
okrag6 = []

def sortujOkregi(e):
    return e[1]

def glosy_komitet(okreg, nr_okregu):
    global lacznie_glosy_komitety
    global lacznie_glosy_okregi
    suma_okreg = 0
    for x, komitet in enumerate(okreg[:6]):
        lacznie_glosy_komitety[x] += int(komitet)
        suma_okreg += int(komitet)
    lacznie_glosy_okregi.append([nr_okregu+1, suma_okreg])

def policz_mandaty(okreg):
    global komitety
    mandaty = [0, 0, 0, 0, 0, 0]
    lacznie_mandatow = int(okreg[-1])
    for i in range(lacznie_mandatow):
        zlicz_krok = []
        for x, glosy in enumerate(okreg[:-1]):
            zlicz_krok.append(int(glosy) / (mandaty[x]+1))
        mandaty[zlicz_krok.index(max(zlicz_krok))] += 1
    return mandaty

def sumuj_mandaty(mandaty):
    for x, mandat in enumerate(mandaty):
        lacznie_mandaty[komitety[x]] += mandat

##MAIN
for x, okreg in enumerate(glosowanie):
    glosy_komitet(okreg, x)
    mandaty_okreg = policz_mandaty(okreg)
    sumuj_mandaty(mandaty_okreg)
    ##Okrag 6
    if x == 5:
        okrag6 = mandaty_okreg


print("-" * 40)
print("1) Poszczegolne komitety otrzymaly nastepujaca liczbe glosow: ")
for x, liczba in enumerate(lacznie_glosy_komitety):
    print("Komitet {}: {}".format(komitety[x], liczba))

lacznie_glosy_okregi.sort(key=sortujOkregi)
print("2) Najwiecej glosow bylo w okregu {}, a najmniej w {}".format(lacznie_glosy_okregi[-1][0], lacznie_glosy_okregi[0][0]))

print("3) Mandaty w Okregu 6:")
for x, mandat in enumerate(okrag6):
    print("Komitet {}: {}".format(komitety[x], mandat))

print("4) Kazdy z komitetow otrzymal lacznie mandatow: ")
for komitet in lacznie_mandaty:
    print("Komitet {}: {}".format(komitet, lacznie_mandaty[komitet]))
