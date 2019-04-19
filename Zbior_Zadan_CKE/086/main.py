with open("DANE/dane_wybory.txt", "r") as file:
    wybory = [line.strip().split() for line in file]

mandaty_najwiecej = {
    "K1": 0,
    "K2": 0,
    "K3": 0,
    "K4": 0,
    "K5": 0
    }

lacznie_mandaty_standard = {
    "K1": 0,
    "K2": 0,
    "K3": 0,
    "K4": 0,
    "K5": 0
    }

lacznie_mandaty_region = {
    "K1": 0,
    "K2": 0,
    "K3": 0,
    "K4": 0,
    "K5": 0
    }

def znajdz_najwieksze(tablica):
    najwieksze = 0
    for x,item in enumerate(tablica):
        if item > tablica[najwieksze]:
            najwieksze = x
    return najwieksze

def oblicz_mandaty(okreg, max_mandatow):
    mandaty = [0, 0, 0, 0, 0,]
    for i in range(max_mandatow):
        tura = [0, 0, 0, 0, 0]
        for x, glosy in enumerate(okreg):
            wynik = int(glosy)/((2*mandaty[x] + 1))
            tura[x] = wynik
        mandaty[znajdz_najwieksze(tura)] += 1
    return mandaty

def polacz_regionalne(okreg):
    global glosy_regionalne
    region = okreg[0][0]
    for x, liczba_glosow in enumerate(okreg[1::]):
        glosy_regionalne[region][x] += int(liczba_glosow)

glosy_regionalne = {
    "A": [0, 0, 0, 0, 0],
    "B": [0, 0, 0, 0, 0],
    "C": [0, 0, 0, 0, 0],
    "D": [0, 0, 0, 0, 0]
    }
for okreg in wybory:
    podzial_standard = oblicz_mandaty(okreg[1::], 20)
    for x, komitet in enumerate(mandaty_najwiecej):
        if podzial_standard[x] > mandaty_najwiecej[komitet]:
            mandaty_najwiecej[komitet] = podzial_standard[x]
    for y, mandat_standard in enumerate(lacznie_mandaty_standard):
        lacznie_mandaty_standard[mandat_standard] += podzial_standard[y]

    polacz_regionalne(okreg)

for metoda_regionalna in list(glosy_regionalne.values()):
    podzial_regionalny = oblicz_mandaty(metoda_regionalna, 100)
    for x, komitet in enumerate(lacznie_mandaty_region):
        lacznie_mandaty_region[komitet] += podzial_regionalny[x]

#Podpunkt 5
def obliczMinimum(m):
    for i in range(100001):
        glosyQ = i
        glosyR = 100000 - i
        wynik = oblicz_mandaty([glosyQ, glosyR], 2*m)   
        if wynik[0] == wynik[1]:
            return i
najmniejM1 = obliczMinimum(10)
najmniejM2 = obliczMinimum(20)
najmniejM3 = obliczMinimum(50)

print("-" * 40)
print("86.3) Maksymalna liczba mandatow dla kazdego komitetu:")
for komitet in mandaty_najwiecej:
    print("{}: {} mandatow".format(komitet, mandaty_najwiecej[komitet]))
print("-" * 20)
print("86.4) Stosujac metode standardowa:")
for komitet in lacznie_mandaty_standard:
    print("{}: {} mandatow".format(komitet, lacznie_mandaty_standard[komitet]))
print("Stosujac metode regionalna:")
for komitet in lacznie_mandaty_region:
    print("{}: {} mandatow".format(komitet, lacznie_mandaty_region[komitet]))
print("-" * 20)
print("86.5)\nDla m = 10: {}\nDla m = 20: {}\nDla m = 50: {}".format(najmniejM1, najmniejM2, najmniejM3))
