od_tylu = []
nowe_hasla = []
def sortuj(e):
    return len(e)


with open("DANE/slowa.txt", "r") as file:
    for line in  file:
        if line.endswith("\n"):
            line = line[:len(line) - 1]

        od_tylu.append(line[::-1])
        for i in range(len(line),0,-1):
            if line[:i] == line[:i][::-1]:
                nowe = line[::-1] + line[i:]
                nowe_hasla.append(nowe)
                break

dlugosc12 = []
najdluzsze = nowe_hasla[0]
najkrotsze = nowe_hasla[0]
suma_dlugosci = 0
for item in nowe_hasla:
    suma_dlugosci += len(item)

    if len(item) == 12:
        dlugosc12.append(item)

    if len(item) > len(najdluzsze):
        najdluzsze = item
    elif len(item) < len(najkrotsze):
        najkrotsze = item

print(dlugosc12, najdluzsze, najkrotsze, suma_dlugosci)


#ZAPISYWANIE WYNIKOW
#A
with open("hasla_a.txt", "w") as fileA:
    fileA.write("\n".join(od_tylu))

od_tylu.sort(reverse=True, key=sortuj)

with open("slowa_a.txt", "w") as fileA2:
    fileA2.write("Najdluzsze haslo {} ma {} znakow \n".format(od_tylu[0], str(len(od_tylu[0]))))
    fileA2.write("Najkrotsze haslo {} ma {} znakow" .format(od_tylu[-1], str(len(od_tylu[-1]))))

#B
with open("hasla_b.txt", "w") as fileB:
    fileB.write("\n".join(nowe_hasla))

with open("slowa_b.txt", "w") as fileB2:
    fileB2.write("Hasla o dlugosci 12: \n{}".format("\n".join(dlugosc12)))
    fileB2.write("\nNajdluzsze haslo {}\n".format(najdluzsze))
    fileB2.write("Najkrotsze haslo {}\n" .format(najkrotsze))
    fileB2.write("Suma dlugosci hasel {}\n" .format(suma_dlugosci))
