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


rewersy = []
najwiecej_czarnych = 0
rekurencyjne = []
for x, obraz in enumerate(wszystko):
    sprawdzRewers = czy_rewers(usun_ramke(obraz))
    if sprawdzRewers[0]:
        rewersy.append(line)
        if sprawdzRewers[1] > najwiecej_czarnych:
            najwiecej_czarnych = sprawdzRewers[1]
    if sprawdz_rekurencje(usun_ramke(obraz)):
        rekurencyjne.append(obraz)

print('-' * 40)
print("Jest {} rewersow, najwieksza liczba pikseli czarnych to {}".format(len(rewersy), najwiecej_czarnych))
print('-' * 40)
print("Jest {} obrazow rekurencyjnych, pierwszy z nich to: ".format(len(rekurencyjne)))
wyswietl(usun_ramke(rekurencyjne[0]))
