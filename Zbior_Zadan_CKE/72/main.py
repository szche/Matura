with open("DANE/napisy.txt", "r") as file:
    wszystko = [line.strip().split() for line in file]

def znajdz_koncowke(para):
    napis1 = para[0]
    napis2 = para[1]
    wspolne = ""
    for x, znak in enumerate(napis2[::-1]):
        if znak == napis1[-(x+1)]:
            wspolne += znak
        else:
            break
    return wspolne[::-1]

dlugosc_3 = []
podpunkt_2 = []
najdluzsza_koncowka = []
najdluzsza_dlugosc = 0
for para in wszystko:
    if len(para[0]) >= 3*len(para[1]) or len(para[1]) >= 3*len(para[0]):
        dlugosc_3.append(para)
    if para[0] == para[1][:len(para[0])]:
        podpunkt_2.append([para, para[1][len(para[0]):]])

    koncowka = znajdz_koncowke(para)
    if len(koncowka) > najdluzsza_dlugosc:
        najdluzsza_dlugosc = len(koncowka)
        najdluzsza_koncowka = []
        najdluzsza_koncowka.append(para)
    elif len(koncowka) == najdluzsza_dlugosc:
        najdluzsza_koncowka.append(para)



    

    
print("-" * 40)
print("72.1) Jest {} par takich napisow, pierwsza z nich to {}".format(len(dlugosc_3), dlugosc_3[0]))
print("72.2):")
for line in podpunkt_2:
    print(line)

print("72.3) Najdluzsza koncowka ma dlugosc {}".format(najdluzsza_dlugosc))
for line in najdluzsza_koncowka:
    print(line)
