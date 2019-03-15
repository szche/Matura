wszystko = []

with open("DANE/dane_obrazki.txt", "r") as file:
    obraz = []
    for line in file:
        if line == "\n":
            wszystko.append(obraz)
            obraz = []
            continue
        obraz.append(line.strip())
    wszystko.append(obraz)

def usun_ramke(obraz):
    nowy_obraz = []
    for line in obraz[:len(obraz)-1]:
        nowy_obraz.append(line[:len(line)-1])
    return nowy_obraz

def czy_rewers(obraz):
    ile_zer = 0
    ile_jedynek = 0
    for line in obraz:
        ile_zer += line.count("0")
        ile_jedynek += line.count("1")
    if ile_jedynek > ile_zer:
        return [True, ile_jedynek]
    return [False, ile_jedynek]

def sprawdz_rekurencje(obraz):
    cwiartka1 = [cwierc[:len(cwierc)//2] for cwierc in obraz[:len(obraz)//2]]
    cwiartka2 = [cwierc[len(cwierc)//2:] for cwierc in obraz[:len(obraz)//2]]
    cwiartka3 = [cwierc[:len(cwierc)//2] for cwierc in obraz[len(obraz)//2:]]
    cwiartka4 = [cwierc[len(cwierc)//2:] for cwierc in obraz[len(obraz)//2:]]
    if cwiartka1 == cwiartka2 and cwiartka1 == cwiartka3 and cwiartka1 == cwiartka4:
        return True
    return False

def wyswietl(obraz):
    for line in obraz:
        print(line)

def wyznacz_pion(obraz, indeks):
    pion = [line[indeks] for line in obraz]
    return "".join(pion)


def sprawdz_poprawnosc(obraz):
    bezRamki = usun_ramke(obraz)
    jestBladPoziom = False
    jestBladPion = False
    for x, poziom in enumerate(bezRamki):
        poziomBit = poziom.count("1")%2
        ramkaPoziom = int(obraz[x][-1])
        
        for y, pion in enumerate(poziom):
            pionBit = wyznacz_pion(bezRamki, y).count("1")%2
            ramkaPion = int(obraz[-1][y])
            if poziomBit != ramkaPoziom and pionBit != ramkaPion:
                return "nienaprawialne"
            if poziomBit != ramkaPoziom:
                jestBladPoziom = True
            if pionBit != ramkaPion:
                jestBladPion = True
    if jestBladPion or jestBladPoziom:
        return "naprawialne"
    return "poprawne"

rewersy = []
najwiecej_czarnych = 0
rekurencyjne = []
poprawne = 0
naprawialne = 0
nienaprawialne = 0
for x, obraz in enumerate(wszystko):
    sprawdzRewers = czy_rewers(usun_ramke(obraz))
    if sprawdzRewers[0]:
        rewersy.append(line)
        if sprawdzRewers[1] > najwiecej_czarnych:
            najwiecej_czarnych = sprawdzRewers[1]
    if sprawdz_rekurencje(usun_ramke(obraz)):
        rekurencyjne.append(obraz)
    if sprawdz_poprawnosc(obraz) == "nienaprawialne":
        nienaprawialne += 1
    elif sprawdz_poprawnosc(obraz) == "naprawialne":
        naprawialne += 1
    elif sprawdz_poprawnosc(obraz) == "poprawne":
        poprawne += 1
print('-' * 40)
print("Jest {} rewersow, najwieksza liczba pikseli czarnych to {}".format(len(rewersy), najwiecej_czarnych))
print('-' * 40)
print("Jest {} obrazow rekurencyjnych, pierwszy z nich to: ".format(len(rekurencyjne)))
wyswietl(usun_ramke(rekurencyjne[0]))
print('-' * 40)
print("Jest {} prawidlowych, {} naprawialnych i {} nienaprawialnych".format(poprawne, naprawialne, nienaprawialne))

